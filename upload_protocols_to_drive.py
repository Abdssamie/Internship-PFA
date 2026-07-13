#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "rich>=13.0",
# ]
# ///
"""
upload_protocols_to_drive.py
============================
Uploads all synthesized protocol PDFs from Internship-PFA to Google Drive
using the `gws` CLI (Google Workspace CLI).

Drive structure created:
    Internship-PFA/
    ├── 01_Dosage_Chlorures_Mohr/
    │   ├── dosage_chlorures.pdf
    │   └── logigramme.pdf
    ├── 02_Determination_Indice_Permanganate/
    │   └── ...
    └── ...

Usage:
    uv run upload_protocols_to_drive.py

Optional env var:
    DRIVE_ROOT_FOLDER_ID=<id>   Upload inside a specific Drive folder
                                instead of My Drive root.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import print as rprint

console = Console()

REPO_ROOT = Path(__file__).parent.resolve()
ROOT_FOLDER_NAME = "Internship-PFA"
PDF_MIME = "application/pdf"
FOLDER_MIME = "application/vnd.google-apps.folder"


# ── gws wrappers ──────────────────────────────────────────────────────────────

def _gws(*args: str) -> dict:
    """Run a gws command and return parsed JSON output. Raises on error."""
    cmd = ["gws", "drive", "files", *args, "--format", "json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        data = {}

    if "error" in data:
        msg = data["error"].get("message", result.stderr or "unknown error")
        raise RuntimeError(msg)

    return data


def find_folder(name: str, parent_id: str | None = None) -> str | None:
    """Search Drive for an existing folder by name (and optional parent). Returns ID or None."""
    q_parts = [f"name = '{name}'", f"mimeType = '{FOLDER_MIME}'", "trashed = false"]
    if parent_id:
        q_parts.append(f"'{parent_id}' in parents")
    q = " and ".join(q_parts)
    data = _gws("list", "--query", q)
    files = data.get("files", [])
    return files[0]["id"] if files else None


def find_or_create_folder(name: str, parent_id: str | None = None) -> tuple[str, bool]:
    """Return (folder_id, created) — reuses existing folder if found, creates otherwise."""
    existing_id = find_folder(name, parent_id)
    if existing_id:
        return existing_id, False
    body: dict = {"name": name, "mimeType": FOLDER_MIME}
    if parent_id:
        body["parents"] = [parent_id]
    data = _gws("create", "--json", json.dumps(body))
    return data["id"], True


def upload_pdf(path: Path, parent_id: str) -> str:
    """Upload a PDF file into a Drive folder and return the file's ID."""
    body = {"name": path.name, "parents": [parent_id]}
    data = _gws(
        "create",
        "--upload", str(path),
        "--upload-content-type", PDF_MIME,
        "--json", json.dumps(body),
    )
    return data["id"]


# ── Discovery ─────────────────────────────────────────────────────────────────

def find_protocol_pdfs() -> dict[str, list[Path]]:
    """
    Return a dict mapping module_dir_name -> sorted list of PDF paths
    found under */protocole/*.pdf (references/ excluded by design).
    """
    modules: dict[str, list[Path]] = {}
    for pdf in sorted(REPO_ROOT.glob("*/protocole/*.pdf")):
        module = pdf.parent.parent.name  # e.g. "03_Determination_de_Lalcalinite"
        modules.setdefault(module, []).append(pdf)
    return modules


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    console.print(Panel.fit(
        "[bold]Internship-PFA — Google Drive Upload[/bold]\n"
        "Powered by [cyan]gws[/cyan] CLI",
        border_style="dim",
    ))

    modules = find_protocol_pdfs()
    total_pdfs = sum(len(v) for v in modules.values())

    if not modules:
        console.print("[red]No protocol PDFs found. Aborting.[/red]")
        sys.exit(1)

    # Preview table
    table = Table(title="PDFs to upload", show_lines=True)
    table.add_column("Module", style="bold cyan")
    table.add_column("Files")
    for module, pdfs in modules.items():
        table.add_row(module, "\n".join(p.name for p in pdfs))
    console.print(table)
    console.print(f"\n[bold]{total_pdfs}[/bold] PDFs across [bold]{len(modules)}[/bold] modules.\n")

    # Root Drive folder
    parent_id: str | None = os.environ.get("DRIVE_ROOT_FOLDER_ID") or None
    console.print(f"[dim]Finding or creating root Drive folder:[/dim] [bold]{ROOT_FOLDER_NAME}[/bold]")
    try:
        root_id, created = find_or_create_folder(ROOT_FOLDER_NAME, parent_id)
    except RuntimeError as e:
        console.print(f"[red]✗ Could not find/create root folder:[/red] {e}")
        sys.exit(1)
    action = "Created" if created else "Reusing existing"
    console.print(f"  [green]✓[/green] {action} root folder ID: [dim]{root_id}[/dim]\n")

    # Upload per module
    errors: list[str] = []
    uploaded = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total} files"),
        console=console,
        transient=False,
    ) as progress:
        overall = progress.add_task("[cyan]Overall", total=total_pdfs)

        for module, pdfs in modules.items():
            progress.print(f"\n[bold]{module}[/bold]")

            # Find or create module sub-folder
            try:
                module_id, mod_created = find_or_create_folder(module, root_id)
                mod_action = "Created" if mod_created else "Reusing"
                progress.print(f"  [dim]{mod_action} folder ID: {module_id}[/dim]")
            except RuntimeError as e:
                progress.print(f"  [red]✗ Folder error:[/red] {e}")
                errors.append(f"{module}/ — folder: {e}")
                progress.advance(overall, len(pdfs))
                continue

            # Upload each PDF
            for pdf in pdfs:
                try:
                    file_id = upload_pdf(pdf, module_id)
                    progress.print(f"  [green]✓[/green] {pdf.name} [dim]({file_id})[/dim]")
                    uploaded += 1
                except RuntimeError as e:
                    progress.print(f"  [red]✗[/red] {pdf.name}: {e}")
                    errors.append(f"{module}/{pdf.name}: {e}")
                finally:
                    progress.advance(overall, 1)

    # Summary
    console.print()
    if errors:
        console.print(Panel(
            "\n".join(f"• {e}" for e in errors),
            title="[red]Failures[/red]",
            border_style="red",
        ))
    console.print(Panel(
        f"[green]{uploaded}/{total_pdfs}[/green] PDFs uploaded successfully.\n"
        f"Root Drive folder: [bold]{ROOT_FOLDER_NAME}[/bold] "
        f"[dim](ID: {root_id})[/dim]",
        title="[bold]Done[/bold]",
        border_style="green" if not errors else "yellow",
    ))

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
