# Organigramme de la Détermination de l'Indice Permanganate (ISO 8467)

Voici l'enchaînement des étapes opératoires et des critères de validation analytiques :

```mermaid
graph TD
    %% Organigramme
    Start([Début de l'analyse]) --> Prep[Préparation : Chauffer le bain-marie à 100 °C]
    Prep --> Dispatch{Type d'analyse ?}

    %% --- CHEMIN A : ÉCHANTILLON ---
    Dispatch -->|Échantillon| A1["<b>1. Préparation & Chauffage</b><br>• Prélever 25,0 mL d'échantillon d'eau<br>• Ajouter 5 mL d'acide sulfurique 2 mol/L (6)<br>• Chauffer au bain-marie à 100 °C pendant 10 min"]
    A1 --> A2["<b>2. Oxydation</b><br>• Ajouter 5,00 mL de KMnO4 0,002 mol/L (2)<br>• Chauffer au bain-marie à 100 °C pendant exactement 10 min"]
    A2 --> A3["<b>3. Réduction & Titrage</b><br>• Ajouter 5,00 mL d'oxalate de sodium 0,005 mol/L (4)<br>• Agiter jusqu'à décoloration complète<br>• Titrer à chaud à ~80 °C avec KMnO4 0,002 mol/L (2)<br>• Enregistrer le volume V1"]

    %% --- CHEMIN B : ESSAI À BLANC & ÉTALONNAGE ---
    Dispatch -->|Blanc & Étalonnage| B1["<b>1. Préparation & Chauffage (Blanc)</b><br>• Prélever 25,0 mL d'eau distillée<br>• Ajouter 5 mL d'acide sulfurique 2 mol/L (6)<br>• Chauffer au bain-marie à 100 °C pendant 10 min"]
    B1 --> B2["<b>2. Oxydation & Réduction (Blanc)</b><br>• Ajouter 5,00 mL de KMnO4 0,002 mol/L (2)<br>• Chauffer au bain-marie à 100 °C pendant exactement 10 min<br>• Ajouter 5,00 mL d'oxalate de sodium 0,005 mol/L (4)<br>• Agiter jusqu'à décoloration complète"]
    B2 --> B3["<b>3. Titrage du Blanc & Étalonnage</b><br>• Titrer à chaud à ~80 °C avec KMnO4 (2) -> <b>Noter V0</b><br>• Ajouter 5,00 mL d'oxalate de sodium (4) dans le même Erlenmeyer<br>• Titrer à chaud à ~80 °C avec KMnO4 (2) -> <b>Noter V2</b>"]

    %% --- CALCULS ---
    A3 --> Calc[Calcul de l'Indice Permanganate :<br>IPM = V1 - V0 / V2 * 16 mg/L O2]
    B3 --> Calc

    %% --- CONTRÔLE QUALITÉ ---
    Calc --> QC1{"V0 <= 0,10 mL ?"}
    QC1 -->|Non| QC_Fail_B["Recommencer l'essai à blanc<br>(Nettoyer la verrerie / eau contaminée)"]
    QC1 -->|Oui| QC2{"Écart duplicatas <= 0,10 mL ?"}
    QC2 -->|Non| QC_Fail_S["Recommencer les titrages<br>(Vérifier la burette)"]
    QC2 -->|Oui| Final([Validation & Rapport d'indice IPM])

    %% Styles
    style Start fill:#fff,stroke:#000,stroke-width:2px;
    style Final fill:#fff,stroke:#000,stroke-width:2px;
    style Dispatch fill:#fff,stroke:#000,stroke-width:2px;
    style QC1 fill:#fff,stroke:#000,stroke-width:2px;
    style QC2 fill:#fff,stroke:#000,stroke-width:2px;
    style Calc fill:#fff,stroke:#000,stroke-width:3px;
    style QC_Fail_B fill:#fff,stroke:#000,stroke-width:2px;
    style QC_Fail_S fill:#fff,stroke:#000,stroke-width:2px;
    
    style A1 text-align:left,fill:#fff,stroke:#000;
    style A2 text-align:left,fill:#fff,stroke:#000;
    style A3 text-align:left,fill:#fff,stroke:#000;
    style B1 text-align:left,fill:#fff,stroke:#000,stroke-dasharray: 5 5;
    style B2 text-align:left,fill:#fff,stroke:#000,stroke-dasharray: 5 5;
    style B3 text-align:left,fill:#fff,stroke:#000,stroke-dasharray: 5 5;
```
