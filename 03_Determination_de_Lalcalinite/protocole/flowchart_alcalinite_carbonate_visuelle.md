# Organigramme de la Détermination de l'Alcalinité Carbonate Visuelle (ISO 9963-2)

Voici l'enchaînement des étapes opératoires et des critères de validation analytiques pour la méthode visuelle uniquement :

```mermaid
graph TD
    %% Début de l'analyse
    Start(["Début de l'analyse"]) --> Prep["Préparer la verrerie de classe A<br>Mettre en place le barbotage de gaz sans CO2"]
    Prep --> Dispatch{"Action à réaliser ?"}

    %% --- ETAPE 1 : ETALONNAGE ACIDE (AVANT UTILISATION) ---
    Dispatch -->|"Étalonnage HCl ~0,020 mol/L"| E1["Pipeter 2,00 mL de Na2CO3 ~0,025 mol/L (3)<br>+ 40 mL d'eau (1) + 3 gouttes d'indicateur mixte (4)<br>Déclencher le barbotage de gaz sans CO2 (2)"]
    E1 --> E2["Titrer avec HCl ~0,020 mol/L (5)<br>jusqu'au virage au gris avec traces de rouge (stable 30 s)<br>Enregistrer le volume V2"]
    E2 --> E2_Check{"3 répétitions faites ?<br>(différence max-min < 0,05 mL)"}
    E2_Check -->|Non| E1
    E2_Check -->|Oui| E3["Titrer le blanc (50 mL d'eau (1) + 3 g. indicateur)<br>dans les mêmes conditions<br>Enregistrer le volume V3"]
    E3 --> E4["Calculer la concentration réelle c(HCl)<br>c(HCl) = 2 * m * V1 / (53,00 * (V2 - V3))"]
    E4 --> E_End["Acide chlorhydrique ~0,020 mol/L étalonné"]

    %% --- ETAPE 2 : DOSAGE DE L'ÉCHANTILLON ---
    Dispatch -->|"Dosage de l'Échantillon"| S1["Pipeter 50,0 mL d'échantillon d'eau (V4)<br>Ajouter 3 gouttes d'indicateur mixte (4)<br>Déclencher le barbotage de gaz sans CO2 (2)"]
    S1 --> S2["Titrer avec HCl ~0,020 mol/L (5)<br>sous barbotage constant jusqu'au virage (gris/rouge)<br>(vérifier la stabilité pendant 30 s)"]
    S2 --> S3["Enregistrer le volume d'acide V5"]
    S3 --> S4{"V5 > 10 mL ?"}
    S4 -->|Oui| S_Reduc["Prendre une prise d'essai V4 plus faible<br>Diluer à 50 mL ± 5 mL avec de l'eau (1)<br>(veiller à ce que le volume consommé >= 3 mL)"]
    S_Reduc --> S2
    S4 -->|Non| S_End["Volume de l'échantillon V5 validé"]

    %% --- ETAPE 3 : ESSAI A BLANC DE LA METHODE ---
    Dispatch -->|"Essai à Blanc"| B1["Introduire 50 mL d'eau purifiée (1)<br>Ajouter 3 gouttes d'indicateur mixte (4)<br>Déclencher le barbotage de gaz sans CO2 (2)"]
    B1 --> B2["Titrer sous barbotage avec HCl (5)<br>jusqu'au virage au gris avec traces de rouge"]
    B2 --> B3["Répéter au moins 3 fois<br>Calculer le volume moyen V6"]
    B3 --> B_End["Essai à blanc de la méthode validé"]

    %% Consolidation finale
    E_End --> Calc
    S_End --> Calc
    B_End --> Calc
    
    Calc["Calculer l'Alcalinité Carbonate A<br>A = c(HCl) * (V5 - V6) * 1000 / V4"] --> Final(["Rapport du résultat :<br>A (mmol/L de H+) avec 2 décimales"])

    %% Styles pour design monochrome
    style Start fill:#fff,stroke:#000,stroke-width:2px;
    style Final fill:#fff,stroke:#000,stroke-width:2px;
    style Dispatch fill:#fff,stroke:#000,stroke-width:2px;
    style E2_Check fill:#fff,stroke:#000,stroke-width:2px;
    style S4 fill:#fff,stroke:#000,stroke-width:2px;
    
    style E1 fill:#fff,stroke:#000,stroke-width:1px;
    style E2 fill:#fff,stroke:#000,stroke-width:1px;
    style E3 fill:#fff,stroke:#000,stroke-width:1px;
    style E4 fill:#fff,stroke:#000,stroke-width:2px;
    
    style S1 fill:#fff,stroke:#000,stroke-width:1px;
    style S2 fill:#fff,stroke:#000,stroke-width:1px;
    style S3 fill:#fff,stroke:#000,stroke-width:1px;
    style S_Reduc fill:#fff,stroke:#000,stroke-width:1px,stroke-dasharray: 5 5;
    style S_End fill:#fff,stroke:#000,stroke-width:2px;
    
    style B1 fill:#fff,stroke:#000,stroke-width:1px;
    style B2 fill:#fff,stroke:#000,stroke-width:1px;
    style B3 fill:#fff,stroke:#000,stroke-width:2px;
    style Calc fill:#fff,stroke:#000,stroke-width:3px;
```
