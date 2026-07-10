# 🧪 Projet de Fin d'Année (PFA) — Protocoles & Analyses Chimiques

Bienvenue dans le dépôt de suivi de mon Projet de Fin d'Année (PFA). Ce projet est structuré autour du développement, de l'optimisation et de la rédaction de protocoles d'analyses chimiques de laboratoire, en s'appuyant sur les normes internationales (notamment les normes ISO).

---

## 📂 Structure du Projet

L'arborescence est organisée de manière modulaire **par méthode d'analyse chimique**. Cela permet de regrouper de façon cohérente les références normatives, les notes de recherche et les protocoles rédigés.

```text
Internship-PFA/
├── README.md                                  # Ce document (guide & tableau de bord)
├── GHS_Pictogrammes/                          # [Partagé] Icônes de sécurité GHS pour les produits chimiques (SVG & PNG)
│   ├── GHS03.svg, GHS05.svg, ...
│   └── README.md                              # Guide d'utilisation et de correspondance des symboles GHS
│
├── 01_Dosage_Chlorures_Mohr/                  # Module : Dosage des ions chlorure (Méthode de Mohr / ISO 9297)
│   ├── references/                            # Norme ISO officielle et notes théoriques
│   │   ├── iso_9297_1989.pdf                  # Norme ISO 9297 de référence
│   │   └── notes_iso_9297_dosage_chlorures.pdf# Synthèse et notes de lecture de la norme
│   └── protocole/                             # Protocole expérimental rédigé
│       ├── dosage_chlorures.typst             # Document source Typst
│       ├── dosage_chlorures.pdf               # Rendu PDF compilé
│       └── fiche_protocole_mohr_iso_9297.pdf  # Fiche pratique de paillasse
│
└── 02_Administratif_et_Suivi/                  # Suivi administratif du stage et de la rédaction
    └── journal_de_bord.md                     # Carnet de suivi hebdomadaire des tâches de stage
```

---

## 🛠️ Outils & Technologies

* **[Typst](https://typst.app/)** : Utilisé pour la rédaction de documents scientifiques et de protocoles. C'est une alternative moderne, rapide et élégante à LaTeX.
* **Normes ISO** : Base scientifique pour la validation des protocoles de dosage.
* **Pictogrammes GHS** : Référentiel réglementaire pour la sécurité chimique au laboratoire.

---

## 🚀 Compilation des Documents Typst

Pour compiler localement le protocole au format PDF :

1. **Installer Typst** (si ce n'est pas déjà fait) :
   * Sur macOS/Linux avec Homebrew : `brew install typst`
   * Sur Ubuntu/Debian : `cargo install typst-cli` ou via le paquet officiel.

2. **Compiler le document** :
   ```bash
   # Pour faire une compilation unique
   typst compile --root . 01_Dosage_Chlorures_Mohr/protocole/dosage_chlorures.typst 01_Dosage_Chlorures_Mohr/protocole/dosage_chlorures.pdf

   # Pour surveiller les modifications en temps réel et recompiler automatiquement
   typst watch --root . 01_Dosage_Chlorures_Mohr/protocole/dosage_chlorures.typst 01_Dosage_Chlorures_Mohr/protocole/dosage_chlorures.pdf
   ```

---

## 📊 Compilation des Flowcharts (Mermaid vers PDF A4)

Les flowcharts sont rédigés en Markdown contenant du code Mermaid (ex: `flowchart.md`). Pour les compiler en un document PDF sur une **page unique A4**, utilisez le script d'extraction et de compilation Typst suivant :

```bash
# 1. Extraire le bloc Mermaid du Markdown
sed -n '/^```mermaid/,/^```/p' protocole/flowchart_methode.md | grep -v '```' > temp.mmd

# 2. Générer le PNG haute résolution (échelle 3 pour une netteté maximale)
npx -y @mermaid-js/mermaid-cli -i temp.mmd -o temp.png -s 3

# 3. Créer un conteneur Typst au format A4
echo '#set page(paper: "a4", margin: 0.5cm); #align(center + horizon)[#image("temp.png", width: 100%, height: 100%, fit: "contain")]' > temp.typst

# 4. Compiler le PDF final
typst compile temp.typst protocole/flowchart.pdf

# 5. Nettoyer les fichiers temporaires
rm temp.mmd temp.png temp.typst
```

---

## 📅 Suivi de Stage & Journal de Bord

Toutes les tâches hebdomadaires, les manipulations effectuées, et les jalons franchis sont documentés dans le [Journal de Bord](file:///home/abdssamie/Internship-PFA/02_Administratif_et_Suivi/journal_de_bord.md).

---

## 🏷️ Nomenclature des Documents

### Signification de `PRO-CHM-001`

`PRO-CHM-001` est un code structuré qui suit une nomenclature standardisée pour le contrôle qualité et la traçabilité des documents de laboratoire :

* **`PRO` (Type de Document)** : Signifie **Protocole** (ou *Procédure*). Indique au lecteur que le document présente une procédure opérationnelle à exécuter sur la paillasse.
* **`CHM` (Domaine Thématique)** : Signifie **Chimie** (Chemistry). Indique le département ou le domaine analytique concerné.
* **`001` (Numéro Séquentiel)** : Indique qu'il s'agit du premier protocole enregistré dans la catégorie Chimie.

---

## 📋 Directives de Rédaction des Fiches de Manipulation

Pour assurer la conformité absolue avec les normes internationales (ex: ISO), appliquez les règles suivantes :
*   **Exactitude normative** : Les fiches doivent décrire uniquement les éléments requis et spécifiés dans la norme ISO associée.
*   **Critères de Contrôle Qualité (QC)** : Les tableaux de critères QC ne sont **pas obligatoires** et ne doivent **pas** être inclus à moins d'être quantitativement exigés par la norme ISO de référence (afin d'éviter d'introduire des critères arbitraires non standardisés).
