# Guide de Rédaction des Protocoles Analytiques (Typst)

Ce document définit les standards de structure et de style que tout agent autonome ou développeur doit respecter lors de la rédaction de fiches de manipulation dans ce dépôt.

---

## 1. Principes Fondamentaux de Style (Monochrome Strict)

*   **Polices de caractères** :
    *   Corps de texte : `STIX Two Text` (police standard des publications scientifiques).
    *   Équations : `STIX Two Math` (garantit un rendu parfait des formules chimiques).
    *   Code et format brut (`raw`) : `Source Code Pro` (taille `9pt`).
*   **Design 100 % monochrome** :
    *   Aucun code couleur (`rgb()`, `luma()`).
    *   Aucun arrière-plan coloré ou gris dans les cellules de tableau ou les blocs.
    *   Aucune bordure arrondie (`radius`).
    *   Tous les tableaux doivent utiliser une bordure noire unifiée de `0.5pt` (`stroke: 0.5pt, fill: none`).
*   **Mise en page** :
    *   Format A4, marges standard de `2.5cm`.
    *   **En-tête** : Titre court du protocole à gauche, Référence + Révision à droite (ex. : `Réf. : PRO-CHM-001 | Rév. : 1.0`), séparé du reste de la page par une ligne noire fine de `0.5pt`.
    *   **Pied de page** : Numéro de page centré au format `Page X / Y` en utilisant un bloc `context` dynamique pour éviter les erreurs de compilation.

---

## 2. Fonctions et Composants Typst Reutilisables

Chaque document `.typst` doit définir en préambule les fonctions suivantes pour structurer les blocs d'avertissement :

```typst
// Boîte de sécurité — bordure gauche épaisse noire, pas de fond
#let safety-box(title: "", content) = {
  block(
    width: 100%,
    stroke: (left: 3pt, rest: 0.5pt),
    inset: (x: 10pt, y: 8pt),
  )[
    #text(weight: "bold")[⚠ #title] \
    #content
  ]
}

// Boîte d'avertissement — bordure gauche épaisse, bordures fines en pointillés, pas de fond
#let warn-box(title: "", content) = {
  block(
    width: 100%,
    stroke: (left: 3pt, rest: (dash: "dashed", thickness: 0.5pt)),
    inset: (x: 10pt, y: 8pt),
  )[
    #text(weight: "bold")[⚑ #title] \
    #content
  ]
}

// Note d'information — simple barre verticale noire à gauche
#let note-box(content) = {
  block(
    width: 100%,
    stroke: (left: 1.5pt, rest: none),
    inset: (left: 12pt, right: 0pt, y: 4pt),
  )[
    #text(weight: "bold")[Note :] #content
  ]
}

// Étape numérotée avec verbe d'action en gras
#let step(verb: "", rest) = {
  block(below: 0.5em)[
    *#verb* #rest
  ]
}
```

---

## 3. Structure Obligatoire des Fiches de Manipulation

Toute fiche de manipulation doit être découpée selon les chapitres suivants :

1.  **Titre principal** : Centré, encadré par deux lignes horizontales noires de `1.5pt`.
2.  **Tableau d'identification** : Tableau à 4 colonnes (`auto, 1fr, auto, 1fr`) contenant :
    *   Référence (ex. : `PRO-CHM-001`).
    *   Révision (`1.0`).
    *   Date d'application (au format `JJ/MM/AAAA`).
    *   Statut (`En vigueur`).
    *   Rédigé par (Nom de l'auteur, fusionné sur 3 colonnes via `table.cell(colspan: 3)`). *Pas de cellule "Approuvé par" tant que le nom du superviseur n'est pas confirmé.*
    *   Domaine d'application et plage de mesure.
3.  **1. Sécurité et Prévention des Risques** :
    *   Contient uniquement le tableau des pictogrammes GHS (`Produit chimique | Pictogramme(s) GHS | Mentions de danger | Conseils de prudence`).
    *   Les pictogrammes GHS doivent être importés comme images depuis le dossier partagé `../GHS_Pictogrammes/` (taille fixe de `30pt`).
    *   Vérifiez attentivement les dangers spécifiques liés aux concentrations de travail (ex: différencier l'irritation légère de la corrosivité forte).
4.  **2. Matériel et Réactifs** :
    *   Tableau **Appareillage** : `Équipement | Capacité / Portée | Classe / Tolérance | Norme de référence` (citer les tolérances de Classe A et les normes ISO associées comme l'ISO 385 pour les burettes).
    *   Tableau **Réactifs** : `Réactif | Concentration | Préparation / Pureté | Conservation` (préciser les conditions de séchage, de température, la sensibilité à la lumière et les contenants appropriés).
5.  **3. Principe de la Méthode** :
    *   Explication concise des réactions chimiques.
    *   Équations équilibrées écrites sous forme de blocs mathématiques Typst avec des symboles de réaction unifiés (ex: flèche de précipitation `↓`).
6.  **4. Mode Opératoire** :
    *   Chaque consigne doit utiliser l'élément `+ #step(verb: "Verbe") [consigne]`.
    *   Chaque étape commence obligatoirement par un **verbe d'action à l'infinitif**.
    *   **Une seule action par étape**.
    *   Mettez en **gras** uniquement les valeurs numériques critiques (ex. : **10,0 mL**, **105 °C**, **10 minutes**).
    *   **Aucune référence à d'autres sections** (ex: ne pas écrire "procéder comme au §4.3"). L'instruction doit être entièrement rédigée et lisible directement.
    *   L'essai à blanc doit être rédigé de façon autonome.
7.  **5. Expression des Résultats** :
    *   Formule de calcul centrée et encadrée (`0.5pt`).
    *   Tableau de définition des variables avec leurs unités.
    *   Tableau des critères QC (uniquement si spécifié quantitativement dans la norme ISO de référence — facultatif sinon, éviter d'ajouter des critères arbitraires non-officiels).
8.  **6. Références Normatives** :
    *   Liste à puces des normes citées (ex: ISO 385, ISO 648, ISO 1042, ISO/CEI 17025).

---

## 4. Prompt à destination de l'agent `02_Determination_Indice_Permanganate`

Lorsqu'un agent doit générer la fiche de manipulation pour le permanganate de potassium, transmettez-lui la consigne suivante :

> Vous êtes chargé de rédiger le protocole de manipulation pour la **Détermination de l'Indice Permanganate dans l'eau** (norme de référence : **ISO 8467**).
>
> Créez le document dans `02_Determination_Indice_Permanganate/protocole/determination_indice_permanganate.typst` en respectant scrupuleusement la charte graphique et les composants définis dans le fichier `AGENTS.md` présent à la racine de l'espace de travail.
>
> Spécificités du protocole à respecter :
> *   **Référence** : `PRO-CHM-002`.
>   **Plage de mesure** : `0,5 mg/L à 10 mg/L` d'oxygène.
> *   **GHS** : Inclure $KMnO_4$ (~0,002 mol/L - comburant/nocif), $H_2SO_4$ (~4 mol/L - corrosif GHS05), et $Na_2C_2O_4$ (oxalate de sodium ~0,005 mol/L - toxique GHS07).
> *   **Appareillage** : Bain-marie thermostaté ($100\ ^\circ\text{C} \pm 2\ ^\circ\text{C}$), verrerie de Classe A (ISO 385, ISO 648, ISO 1042).
> *   **Mode Opératoire** : Décrire l'oxydation à chaud, le titrage de l'excès, et l'essai à blanc de manière indépendante avec des verbes d'action.
> *   **Résultats** : Formule de calcul de l'indice permanganate.
>
> Compilation finale à valider avec la commande :
> `typst compile --root ../../ protocole/determination_indice_permanganate.typst`

---

## 5. Compilation des Flowcharts (Mermaid vers PDF A4 Unique)

Pour garantir qu'un flowchart rédigé en Mermaid s'intègre parfaitement sur une **page unique au format A4** (sans coupure ni pagination aberrante), respectez scrupuleusement la procédure suivante :

1. **Extraction du code Mermaid** : Extraire le bloc de code Mermaid depuis le fichier Markdown dans un fichier temporaire `.mmd` :
   ```bash
   sed -n '/^```mermaid/,/^```/p' protocole/flowchart_alcalinite.md | grep -v '```' > temp.mmd
   ```

2. **Rendu en image haute résolution (PNG)** : Compiler le fichier `.mmd` en un fichier image PNG en utilisant un facteur d'échelle de 3 (`-s 3`) pour garantir la netteté du texte (évitez le format SVG dont le rendu des objets HTML foreignObject peut poser problème lors de l'intégration dans Typst) :
   ```bash
   npx -y @mermaid-js/mermaid-cli -i temp.mmd -o temp.png -s 3
   ```

3. **Création du conteneur Typst temporaire** : Générer un fichier `.typst` configurant le format A4 et insérant l'image avec un ajustement automatique (`fit: "contain"`) :
   ```bash
   echo '#set page(paper: "a4", margin: 0.5cm); #align(center + horizon)[#image("temp.png", width: 100%, height: 100%, fit: "contain")]' > temp.typst
   ```

4. **Compilation finale en PDF** : Compiler le fichier `.typst` pour obtenir le PDF du flowchart sur une page A4 unique :
   ```bash
   typst compile temp.typst protocole/flowchart.pdf
   ```

5. **Nettoyage des fichiers temporaires** :
   ```bash
   rm temp.mmd temp.png temp.typst
   ```

