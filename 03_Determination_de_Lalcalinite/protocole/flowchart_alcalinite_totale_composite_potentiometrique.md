# Organigramme de la Détermination de l'Alcalinité Potentiométrique (ISO 9963-1)

Voici l'enchaînement des étapes opératoires et des critères de validation analytiques pour la méthode potentiométrique uniquement :

```mermaid
graph TD
    %% Début de l'analyse
    Start(["Début de l'analyse"]) --> Prep["Préparer & Calibrer le pH-mètre<br>(tampons pH 4, 7 et 9)"]
    Prep --> Dispatch{"Action à réaliser ?"}

    %% --- ETAPE 1 : ETALONNAGE ACIDE (HEBDOMADAIRE) ---
    Dispatch -->|"Étalonnage HCl ~0,1 mol/L"| E1["Prélever 25,0 mL de Na2CO3 0,025 mol/L (2)<br>+ 75 mL d'eau purifiée (1)"]
    E1 --> E2["Titrer avec HCl ~0,1 mol/L (3)<br>jusqu'à pH 4,5 ± 0,05 -> Enregistrer V2"]
    E2 --> E3["Titrer le blanc (100 mL eau purifiée)<br>Enregistrer le volume consommé V3"]
    E3 --> E4["Calculer concentration réelle c(HCl, 1)<br>c(HCl, 1) = m * V1 / (53,00 * (V2 - V3))"]
    E4 --> E_End["Acide chlorhydrique ~0,1 mol/L étalonné"]

    %% --- ETAPE 2 : PREPARATION ACIDE FAIBLE ---
    Dispatch -->|"Préparation HCl ~0,02 mol/L"| P1["Pipeter 100 mL de HCl ~0,1 mol/L (3)<br>diluer à 500 mL dans fiole jaugée"]
    P1 --> P2["Calculer concentration réelle c(HCl, 2)<br>c(HCl, 2) = 0,2 * c(HCl, 1)"]
    P2 --> P_End["Acide chlorhydrique ~0,02 mol/L prêt<br>(À préparer extemporanément)"]

    %% --- ETAPE 3 : ANALYSE ÉCHANTILLON ---
    Dispatch -->|"Dosage de l'Échantillon"| S1["Pipeter 100,0 mL d'échantillon d'eau (V4)<br>Mesurer le pH initial (pHi) sous agitation"]
    S1 --> S2{"pHi >= 8,3 ?"}

    %% Branche pHi < 8,3 (Pas d'alcalinité composite)
    S2 -->|Non| S_Ap_Zero["Alcalinité composite Ap = 0 mmol/L"]
    S_Ap_Zero --> S_Tit_AT

    %% Branche pHi >= 8,3 (Alcalinité composite présente)
    S2 -->|Oui| S_Select["Sélectionner concentration d'acide :<br>HCl ~0,1 mol/L (si 4 à 20 mmol/L)<br>HCl ~0,02 mol/L (si 0,4 à 4 mmol/L)"]
    S_Select --> S_Tit_Ap["Titrer jusqu'à pH 8,3 ± 0,05<br>Enregistrer le volume Vs"]
    S_Tit_Ap --> S_Tit_AT["Titrer (suite) jusqu'à pH 4,5 ± 0,05<br>(attendre 30 s près du point final)"]

    %% Enregistrement et Validation
    S_Ap_Zero --> S_Tit_AT
    S_Tit_AT --> S_Rec_Ve["Enregistrer le volume total Ve"]
    S_Rec_Ve --> Calc["Calculer Ap et AT dans les conditions conformes"]

    %% Consolidation finale
    E_End --> Calc
    P_End --> Calc
    Calc --> Final(["Rapport du résultat :<br>Ap (mmol/L) & AT (mmol/L)"])

    %% Styles pour design monochrome
    style Start fill:#fff,stroke:#000,stroke-width:2px;
    style Final fill:#fff,stroke:#000,stroke-width:2px;
    style Dispatch fill:#fff,stroke:#000,stroke-width:2px;
    style S2 fill:#fff,stroke:#000,stroke-width:2px;
    
    style E1 fill:#fff,stroke:#000,stroke-width:1px;
    style E2 fill:#fff,stroke:#000,stroke-width:1px;
    style E3 fill:#fff,stroke:#000,stroke-width:1px;
    style E4 fill:#fff,stroke:#000,stroke-width:2px;
    
    style P1 fill:#fff,stroke:#000,stroke-width:1px;
    style P2 fill:#fff,stroke:#000,stroke-width:2px;
    
    style S1 fill:#fff,stroke:#000,stroke-width:1px;
    style S_Ap_Zero fill:#fff,stroke:#000,stroke-width:2px,stroke-dasharray: 5 5;
    style S_Select fill:#fff,stroke:#000,stroke-width:1px;
    style S_Tit_Ap fill:#fff,stroke:#000,stroke-width:1px;
    style S_Tit_AT fill:#fff,stroke:#000,stroke-width:1px;
    style S_Rec_Ve fill:#fff,stroke:#000,stroke-width:1px;
    style Calc fill:#fff,stroke:#000,stroke-width:3px;
```
