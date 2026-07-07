# Pictogrammes GHS — Référence Rapide

Source : [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:GHS_pictograms) — Licence Creative Commons CC BY-SA

## Pictogrammes disponibles

| Code   | Nom officiel (FR)            | Symbole           | Fichiers disponibles                |
|--------|------------------------------|-------------------|-------------------------------------|
| GHS03  | Comburant                    | Flamme sur cercle | `GHS03.svg`, `GHS03.png`, `GHS03_hq.png` |
| GHS05  | Corrosif                     | Corrosion         | `GHS05.svg`, `GHS05.png`, `GHS05_hq.png` |
| GHS07  | Attention (point d'excl.)    | Point d'exclamation | `GHS07.svg`, `GHS07.png`, `GHS07_hq.png` |
| GHS08  | Danger pour la santé         | Silhouette humaine | `GHS08.svg`, `GHS08.png`, `GHS08_hq.png` |
| GHS09  | Danger pour l'environnement  | Arbre/poisson     | `GHS09.svg`, `GHS09.png`, `GHS09_hq.png` |

## Format recommandé selon usage

| Document         | Format recommandé                      |
|------------------|----------------------------------------|
| LaTeX / PDF      | `GHS0X.svg` (via `\includesvg`)        |
| Word / LibreOffice | `GHS0X_hq.png` (500×500 px, 300 DPI) |
| HTML / Web       | `GHS0X.svg` (vectoriel)               |
| Impression basse résolution | `GHS0X.png` (200×200 px)  |

## Utilisation dans les produits chimiques du protocole

| Produit chimique              | Pictogrammes GHS        |
|-------------------------------|-------------------------|
| Nitrate d'argent (AgNO₃)      | GHS03, GHS05, GHS09     |
| Chromate de potassium (K₂CrO₄)| GHS07, GHS08, GHS09     |
| Acide nitrique (HNO₃ 0,1 mol/L) | GHS05               |
| Hydroxyde de sodium (NaOH 0,1 mol/L) | GHS05          |

## Exemple d'intégration LaTeX

```latex
\usepackage{svg}
% Dans le tableau :
\includesvg[width=1.5cm]{GHS_Pictogrammes/GHS05}
```

## Exemple d'intégration HTML

```html
<img src="GHS_Pictogrammes/GHS05.svg" alt="GHS05 - Corrosif" width="60" height="60">
```
