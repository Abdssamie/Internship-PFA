# Organigramme de la Détermination de l'Alcalinité Visuelle (ISO 9963-1)

Voici l'enchaînement des étapes opératoires et des critères de validation analytiques pour la méthode visuelle uniquement :

```mermaid
graph TD
    %% Début de l'analyse
    Start(["Début de l'analyse"]) --> Prep["Préparer la verrerie de classe A<br>et la capsule en porcelaine blanche"]
    Prep --> Dispatch{"Action à réaliser ?"}

    %% --- ETAPE 1 : ETALONNAGE ACIDE (HEBDOMADAIRE) ---
    Dispatch -->|"Étalonnage HCl ~0,1 mol/L"| E1["Prélever 25,0 mL de Na2CO3 0,025 mol/L (2)<br>+ 75 mL d'eau + 0,1 mL d'indicateur mixte (6)"]
    E1 --> E2["Titrer avec HCl ~0,1 mol/L (3) jusqu'à disparition<br>de la couleur bleu-vert (virage) -> Enregistrer V2"]
    E2 --> E3["Titrer le blanc (100 mL d'eau + 0,1 mL indicateur)<br>avec même HCl -> Enregistrer V3"]
    E3 --> E4["Calculer la concentration exacte c(HCl, 1)<br>c(HCl, 1) = m * V1 / (53,00 * (V2 - V3))"]
    E4 --> E_End["Acide chlorhydrique ~0,1 mol/L étalonné"]

    %% --- ETAPE 2 : PREPARATION ACIDE FAIBLE ---
    Dispatch -->|"Préparation HCl ~0,02 mol/L"| P1["Pipeter 100 mL de HCl ~0,1 mol/L (3)<br>diluer à 500 mL dans fiole jaugée"]
    P1 --> P2["Calculer la concentration exacte c(HCl, 2)<br>c(HCl, 2) = 0,2 * c(HCl, 1)"]
    P2 --> P_End["Acide chlorhydrique ~0,02 mol/L prêt<br>(À préparer extemporanément)"]

    %% --- ETAPE 3 : ANALYSE ÉCHANTILLON ---
    Dispatch -->|"Dosage de l'Échantillon"| S0["Chlore libre présent ?<br>Si oui: Ajouter 0,05 mL de thiosulfate de sodium (7)"]
    S0 --> S1["Pipeter 100,0 mL d'échantillon d'eau (V4)<br>+ 0,1 mL d'indicateur phénolphtaléine (5)"]
    S1 --> S2{"Coloration rose ?"}

    %% Branche pHi < 8,3 (Pas d'alcalinité composite)
    S2 -->|Non| S_Ap_Zero["Alcalinité composite Ap = 0 mmol/L<br>+ Ajouter 0,1 mL d'indicateur mixte (6)"]
    S_Ap_Zero --> S_Tit_AT["Titrer avec HCl ~0,1 ou ~0,02 mol/L<br>jusqu'au virage du vert-bleu au gris"]

    %% Branche pHi >= 8,3 (Alcalinité composite présente)
    S2 -->|Oui| S_Select["Sélectionner concentration d'acide :<br>HCl ~0,1 mol/L (si 4 à 20 mmol/L)<br>HCl ~0,02 mol/L (si 0,4 à 4 mmol/L)"]
    S_Select --> S_Tit_Ap["Titrer jusqu'à la décoloration complète du rose<br>Enregistrer le volume Vs<br>+ Ajouter 0,1 mL d'indicateur mixte (6)"]
    S_Tit_Ap --> S_Tit_AT

    %% Enregistrement et Validation
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
    
    style S0 fill:#fff,stroke:#000,stroke-width:1px;
    style S1 fill:#fff,stroke:#000,stroke-width:1px;
    style S_Ap_Zero fill:#fff,stroke:#000,stroke-width:2px,stroke-dasharray: 5 5;
    style S_Select fill:#fff,stroke:#000,stroke-width:1px;
    style S_Tit_Ap fill:#fff,stroke:#000,stroke-width:1px;
    style S_Tit_AT fill:#fff,stroke:#000,stroke-width:1px;
    style S_Rec_Ve fill:#fff,stroke:#000,stroke-width:1px;
    style Calc fill:#fff,stroke:#000,stroke-width:3px;
```
