# Organigramme de la Détermination de l'Alcalinité Visuelle (ISO 9963-1)

Voici l'enchaînement des étapes opératoires et des critères de validation analytiques pour la méthode visuelle uniquement :

```mermaid
graph LR
    %% Début de l'analyse
    Start(["Début de l'analyse"]) --> Prep["Préparer la verrerie de classe A<br>et la capsule en porcelaine blanche"]
    Prep --> Dispatch{"Action à réaliser ?"}

    %% --- ETAPE 1 : ETALONNAGE ACIDE (HEBDOMADAIRE) ---
    Dispatch -->|"Étalonnage HCl ~0,1 mol/L"| E1["Prélever 25,0 mL de Na2CO3 0,025 mol/L"]
    E1 --> E2["Ajouter 75 mL d'eau de qualité 2<br>+ 0,1 mL d'indicateur mixte (5.6)"]
    E2 --> E3["Titrer avec HCl ~0,1 mol/L jusqu'à disparition<br>de la couleur bleu-vert (virage)"]
    E3 --> E4["Enregistrer le volume consommé V2"]
    E4 --> E5["Titrer le blanc (100 mL eau de qualité 2)<br>Enregistrer le volume V3"]
    E5 --> E6["Calculer la concentration exacte c(HCl, 1)<br>c(HCl, 1) = m * V1 / (53,00 * (V2 - V3))"]
    E6 --> E_End["Acide chlorhydrique ~0,1 mol/L étalonné"]

    %% --- ETAPE 2 : PREPARATION ACIDE FAIBLE ---
    Dispatch -->|"Préparation HCl ~0,02 mol/L"| P1["Pipeter 100 mL de HCl ~0,1 mol/L dans fiole jaugée 500 mL"]
    P1 --> P2["Compléter au trait de jauge avec eau de qualité 2"]
    P2 --> P3["Calculer la concentration exacte c(HCl, 2)<br>c(HCl, 2) = 0,2 * c(HCl, 1)"]
    P3 --> P_End["Acide chlorhydrique ~0,02 mol/L prêt<br>(À préparer extemporanément)"]

    %% --- ETAPE 3 : ANALYSE ÉCHANTILLON ---
    Dispatch -->|"Dosage de l'Échantillon"| S_Pre{"Chlore libre présent ?"}
    S_Pre -->|Oui| S_Thio["Ajouter 0,1 mL de thiosulfate de sodium (5.7)<br>pour 200 mL d'échantillon"]
    S_Pre -->|Non| S1["Pipeter 100,0 mL d'échantillon d'eau (V4)"]
    S_Thio --> S1
    S1 --> S2["Ajouter 0,1 mL d'indicateur phénolphtaléine (5.5)"]
    S2 --> S3{"Coloration rose ?"}

    %% Branche pHi < 8,3 (Pas d'alcalinité composite)
    S3 -->|Non| S_Ap_Zero["Alcalinité composite Ap = 0 mmol/L"]
    S_Ap_Zero --> S_Ind_Mix["Ajouter 0,1 mL d'indicateur mixte (5.6)"]
    S_Ind_Mix --> S_Tit_AT["Titrer avec HCl ~0,1 ou ~0,02 mol/L<br>jusqu'au virage du vert-bleu au gris"]

    %% Branche pHi >= 8,3 (Alcalinité composite présente)
    S3 -->|Oui| S_Select["Sélectionner la concentration d'acide"]
    S_Select -->|4 à 20 mmol/L| S_Acid_Fort["Utiliser HCl ~0,1 mol/L"]
    S_Select -->|0,4 à 4 mmol/L| S_Acid_Faible["Utiliser HCl ~0,02 mol/L"]
    S_Acid_Fort & S_Acid_Faible --> S_Tit_Ap["Titrer jusqu'à la décoloration complète du rose"]
    S_Tit_Ap --> S_Rec_Vs["Enregistrer le volume Vs d'acide consommé"]
    S_Rec_Vs --> S_Ind_Mix

    %% Enregistrement et Validation
    S_Tit_AT --> S_Rec_Ve["Enregistrer le volume total Ve d'acide consommé"]
    S_Rec_Ve --> QC{"Duplicatas validés ?<br>|Ve1 - Ve2| <= 0,10 mL"}
    QC -->|Non| QC_Fail["Vérifier la burette/lumière<br>et répéter le titrage"]
    QC -->|Oui| Calc["Calculer Ap et AT dans les conditions conformes"]

    %% Consolidation finale
    E_End --> Calc
    P_End --> Calc
    Calc --> Final(["Rapport du résultat :<br>Ap (mmol/L) & AT (mmol/L)"])

    %% Styles pour compatibilité et design monochrome
    style Start fill:#fff,stroke:#000,stroke-width:2px;
    style Final fill:#fff,stroke:#000,stroke-width:2px;
    style Dispatch fill:#fff,stroke:#000,stroke-width:2px;
    style S3 fill:#fff,stroke:#000,stroke-width:2px;
    style S_Pre fill:#fff,stroke:#000,stroke-width:2px;
    style S_Select fill:#fff,stroke:#000,stroke-width:2px;
    style QC fill:#fff,stroke:#000,stroke-width:2px;
    style QC_Fail fill:#fff,stroke:#000,stroke-width:3px;
    
    style E1 fill:#fff,stroke:#000,stroke-width:1px;
    style E2 fill:#fff,stroke:#000,stroke-width:1px;
    style E3 fill:#fff,stroke:#000,stroke-width:1px;
    style E4 fill:#fff,stroke:#000,stroke-width:1px;
    style E5 fill:#fff,stroke:#000,stroke-width:1px;
    style E6 fill:#fff,stroke:#000,stroke-width:2px;
    
    style P1 fill:#fff,stroke:#000,stroke-width:1px;
    style P2 fill:#fff,stroke:#000,stroke-width:1px;
    style P3 fill:#fff,stroke:#000,stroke-width:2px;
    
    style S1 fill:#fff,stroke:#000,stroke-width:1px;
    style S2 fill:#fff,stroke:#000,stroke-width:1px;
    style S_Thio fill:#fff,stroke:#000,stroke-width:1px;
    style S_Ap_Zero fill:#fff,stroke:#000,stroke-width:2px,stroke-dasharray: 5 5;
    style S_Ind_Mix fill:#fff,stroke:#000,stroke-width:1px;
    style S_Tit_Ap fill:#fff,stroke:#000,stroke-width:1px;
    style S_Rec_Vs fill:#fff,stroke:#000,stroke-width:1px;
    style S_Tit_AT fill:#fff,stroke:#000,stroke-width:1px;
    style S_Rec_Ve fill:#fff,stroke:#000,stroke-width:1px;
    style Calc fill:#fff,stroke:#000,stroke-width:3px;
```
