# Organigramme du Dosage des Nitrites par Spectrométrie d'Absorption (ISO 6777)

Voici l'enchaînement des étapes opératoires et des critères de validation analytiques pour le dosage des nitrites :

```mermaid
graph TD
    %% Début de l'analyse
    Start(["Début de l'analyse"]) --> Prep["Laver la verrerie à l'HCl ~2 mol/L et rincer abondamment<br>Mettre en marche le spectrophotomètre (540 nm)"]
    Prep --> Dispatch{"Action à réaliser ?"}

    %% --- ETAPE 1 : ETALONNAGE / VERIFICATION DE LA SOLUTION STOCK ---
    Dispatch -->|"Étalonnage solution stock"| E1["Pipeter 50,0 mL de KMnO4 0,01 mol/L (7)<br>+ 10 mL H2SO4 2,5 mol/L (8) dans fiole conique de 250 mL"]
    E1 --> E2["Remplir burette de solution nitrite stock (5)<br>Plonger l'extrémité sous la surface du liquide acide"]
    E2 --> E3["Titrer lentement jusqu'à décoloration presque complète<br>Chauffer à ~40 °C et titrer jusqu'au virage incolore"]
    E3 --> E4["Noter le volume consommé (V_titrage)"]
    E4 --> E_Check{"35,02 mL ± 0,40 mL ?"}
    E_Check -->|Non| E_Reject["Rejeter la solution stock<br>Préparer une nouvelle solution (5)"]
    E_Reject --> E1
    E_Check -->|Oui| E_End["Solution stock validée<br>Préparer la solution de travail (6)"]

    %% --- ETAPE 2 : COURBE D'ÉTALONNAGE ---
    Dispatch -->|"Courbe d'étalonnage"| C1["Préparer 9 fioles jaugées de 50 mL<br>Ajouter les volumes de solution de travail (6) :<br>0,00 ; 0,50 ; 1,00 ; 1,50 ; 2,00 ; 2,50 ; 5,00 ; 7,50 ; 10,00 mL"]
    C1 --> C2["Ajuster chaque fiole à 40 ± 2 mL avec de l'eau (1)"]
    C2 --> C3["Ajouter 1,0 mL de réactif coloré (4)<br>Homogénéiser immédiatement par rotation"]
    C3 --> C4["Compléter à 50 mL avec de l'eau (1)<br>Laisser reposer 20 min à l'obscurité"]
    C4 --> C5["Mesurer l'absorbance à 540 nm contre l'eau :<br>- Cuves de 40 mm pour les fioles 1 à 6 (gamme 0–2,50 µg N)<br>- Cuves de 10 mm pour les fioles 1, 3, 6, 7, 8, 9 (gamme 0–10,00 µg N)"]
    C5 --> C6["Soustruire le blanc (fiole 1) & tracer la courbe linéaire<br>(doit passer par l'origine)"]
    C6 --> C_End["Courbe d'étalonnage prête"]

    %% --- ETAPE 3 : DOSAGE DE L'ÉCHANTILLON ---
    Dispatch -->|"Dosage de l'Échantillon"| S1["Prétraiter si besoin (décantation/filtration sur fibre de verre)<br>Pipeter la prise d'essai (V <= 40 mL) dans fiole de 50 mL"]
    S1 --> S2["Ajuster le volume à 40 ± 2 mL avec de l'eau (1)"]
    S2 --> S3["Ajouter 1,0 mL de réactif coloré (4)<br>Homogénéiser immédiatement par rotation"]
    S3 --> S4["Compléter à 50 mL avec de l'eau (1)<br>Laisser reposer 20 min à l'obscurité"]
    S4 --> S5["Mesurer l'absorbance à 540 nm contre l'eau -> Noter As"]
    
    %% Blanc et corrections
    S5 --> B1["Réaliser le blanc de la méthode : 40 mL d'eau (1) + 1,0 mL réactif (4)<br>Traiter et mesurer -> Noter Ab"]
    S5 --> B2["Si échantillon coloré, réaliser le blanc de coloration :<br>Prise d'essai V + 1,0 mL H3PO4 dilué (3) au lieu du réactif (4)<br>Traiter et mesurer -> Noter Ac"]
    
    B1 --> S_End
    B2 --> S_End
    S_End["Volumes & Absorbances de l'échantillon prêts"]

    %% Consolidation finale
    E_End --> Calc
    C_End --> Calc
    S_End --> Calc
    
    Calc["Calculer l'absorbance corrigée Ar :<br>Ar = As - Ab (sans correction couleur)<br>Ar = As - Ab - Ac (avec correction couleur)"] --> Calc2["Déterminer la masse m_N (µg N) correspondante sur la courbe"]
    Calc2 --> Calc3["Calculer la concentration en azote nitrique :<br>rho_N = m_N / V"]
    Calc3 --> Final(["Rapport du résultat :<br>rho_N (mg/L N) ou rho_NO2- (mg/L)<br>(précision de deux décimales)"])

    %% Styles pour design monochrome
    style Start fill:#fff,stroke:#000,stroke-width:2px;
    style Final fill:#fff,stroke:#000,stroke-width:2px;
    style Dispatch fill:#fff,stroke:#000,stroke-width:2px;
    style E_Check fill:#fff,stroke:#000,stroke-width:2px;
    
    style E1 fill:#fff,stroke:#000,stroke-width:1px;
    style E2 fill:#fff,stroke:#000,stroke-width:1px;
    style E3 fill:#fff,stroke:#000,stroke-width:1px;
    style E4 fill:#fff,stroke:#000,stroke-width:1px;
    style E_Reject fill:#fff,stroke:#000,stroke-width:1px,stroke-dasharray: 5 5;
    style E_End fill:#fff,stroke:#000,stroke-width:2px;
    
    style C1 fill:#fff,stroke:#000,stroke-width:1px;
    style C2 fill:#fff,stroke:#000,stroke-width:1px;
    style C3 fill:#fff,stroke:#000,stroke-width:1px;
    style C4 fill:#fff,stroke:#000,stroke-width:1px;
    style C5 fill:#fff,stroke:#000,stroke-width:1px;
    style C6 fill:#fff,stroke:#000,stroke-width:2px;
    style C_End fill:#fff,stroke:#000,stroke-width:2px;
    
    style S1 fill:#fff,stroke:#000,stroke-width:1px;
    style S2 fill:#fff,stroke:#000,stroke-width:1px;
    style S3 fill:#fff,stroke:#000,stroke-width:1px;
    style S4 fill:#fff,stroke:#000,stroke-width:1px;
    style S5 fill:#fff,stroke:#000,stroke-width:1px;
    
    style B1 fill:#fff,stroke:#000,stroke-width:1px;
    style B2 fill:#fff,stroke:#000,stroke-width:1px;
    style S_End fill:#fff,stroke:#000,stroke-width:2px;
    
    style Calc fill:#fff,stroke:#000,stroke-width:1px;
    style Calc2 fill:#fff,stroke:#000,stroke-width:1px;
    style Calc3 fill:#fff,stroke:#000,stroke-width:3px;
```
