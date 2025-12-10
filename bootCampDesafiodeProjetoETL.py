# Projeto ETL – BootCamp Santander 2025
#Extract: leitura dos dados do Excel
#Transform: cálculo dos coeficientes de Steinhart-Hart
#Load: escrita dos coeficientes em nova aba do Excel


# PROGRAMA PARA OBTER OS PARÂMETROS (A, B, C) DA EQUAÇÃO DE STEINHAR-HART UTILIZANDO OS SENSORES 
# NAS TEMPERATURAS DE  20.5°C, 35.5°C E 50.5°C
# PELO MÉTODO DA SUBSTITUIÇÃO DIRETA

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PARÂMETROS PARA O SENSOR 0 (POSIÇÃO 0 NA BARRA METÁLICA):

import numpy as np
import pandas as pd

# EXTRACT
df = pd.read_excel("GitHub\\DesafioETL\\calibracao_sensores.xlsx", sheet_name="Dados")

# Dados de calibração (3 pontos):
# EXTRACT
resistencias = df.loc[0, ["R1", "R2", "R3"]].tolist()
temperaturas = df.loc[0, ["T1", "T2", "T3"]].tolist()

# A equação de Steinhart-Hart é expressa como:1/T = A + B * ln(R) + C * ln(R)^3

def substituicao_simples(resistencias, temperaturas):
    """Calcula os coeficientes A, B e C usando substituição simples."""
    T1 = temperaturas[0] + 273.15
    T2 = temperaturas[1] + 273.15
    T3 = temperaturas[2] + 273.15

    R1 = resistencias[0]
    R2 = resistencias[1]
    R3 = resistencias[2]

    L1 = np.log(R1)
    L2 = np.log(R2)
    L3 = np.log(R3)

    G1 = 1.0 / T1
    G2 = 1.0 / T2
    G3 = 1.0 / T3

    C0 = ((G3 - G1) * (L1 - L2) - (G2 - G1) * (L1 - L3)) / ((L1 - L2) * (L1**3 - L3**3) - (L1 - L3) * (L1**3 - L2**3))
    B0 = ((G2 - G1) - C0 * (L2**3 - L1**3)) / (L2 - L1)
    A0 = G1 - B0 * L1 - C0 * L1**3

    return A0, B0, C0


# Calcular coeficientes
coeficientes0 = substituicao_simples(resistencias, temperaturas)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PARÂMETROS PARA O SENSOR 1 (POSIÇÃO 1 NA BARRA METÁLICA):


# Dados de calibração (3 pontos)
# EXTRACT
resistencias = df.loc[1, ["R1", "R2", "R3"]].tolist()
temperaturas = df.loc[1, ["T1", "T2", "T3"]].tolist()

# A equação de Steinhart-Hart é expressa como:1/T = A + B * ln(R) + C * ln(R)^3

def substituicao_simples(resistencias, temperaturas):
    """Calcula os coeficientes A, B e C usando substituição simples."""
    T1 = temperaturas[0] + 273.15
    T2 = temperaturas[1] + 273.15
    T3 = temperaturas[2] + 273.15

    R1 = resistencias[0]
    R2 = resistencias[1]
    R3 = resistencias[2]

    L1 = np.log(R1)
    L2 = np.log(R2)
    L3 = np.log(R3)

    G1 = 1.0 / T1
    G2 = 1.0 / T2
    G3 = 1.0 / T3

    C1 = ((G3 - G1) * (L1 - L2) - (G2 - G1) * (L1 - L3)) / ((L1 - L2) * (L1**3 - L3**3) - (L1 - L3) * (L1**3 - L2**3))
    B1 = ((G2 - G1) - C1 * (L2**3 - L1**3)) / (L2 - L1)
    A1 = G1 - B1 * L1 - C1 * L1**3

    return A1, B1, C1


# Calcular coeficientes
coeficientes1 = substituicao_simples(resistencias, temperaturas)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# PARÂMETROS PARA O SENSOR 2 (POSIÇÃO 2 NA BARRA METÁLICA):


# Dados de calibração (3 pontos)
# EXTRACT
resistencias = df.loc[2, ["R1", "R2", "R3"]].tolist()
temperaturas = df.loc[2, ["T1", "T2", "T3"]].tolist()

# A equação de Steinhart-Hart é expressa como:1/T = A + B * ln(R) + C * ln(R)^3

def substituicao_simples(resistencias, temperaturas):
    """Calcula os coeficientes A, B e C usando substituição simples."""
    T1 = temperaturas[0] + 273.15
    T2 = temperaturas[1] + 273.15
    T3 = temperaturas[2] + 273.15

    R1 = resistencias[0]
    R2 = resistencias[1]
    R3 = resistencias[2]

    L1 = np.log(R1)
    L2 = np.log(R2)
    L3 = np.log(R3)

    G1 = 1.0 / T1
    G2 = 1.0 / T2
    G3 = 1.0 / T3

    C2 = ((G3 - G1) * (L1 - L2) - (G2 - G1) * (L1 - L3)) / ((L1 - L2) * (L1**3 - L3**3) - (L1 - L3) * (L1**3 - L2**3))
    B2 = ((G2 - G1) - C2 * (L2**3 - L1**3)) / (L2 - L1)
    A2 = G1 - B2 * L1 - C2 * L1**3

    return A2, B2, C2


# Calcular coeficientes
coeficientes2 = substituicao_simples(resistencias, temperaturas)

# TRANSFORM
print("================= ✨ MÉTODO DA SUBSTITUIÇÃO DIRETA PARA 3 SENSORES ✨ ====================================")
print(" ")

coeficientes = { 
    "Sensor": ["S0", "S1", "S2"], 
    "A": [coeficientes0[0], coeficientes1[0], coeficientes2[0]], 
    "B": [coeficientes0[1], coeficientes1[1], coeficientes2[1]], 
    "C": [coeficientes0[2], coeficientes1[2], coeficientes2[2]] 
    } 
df_coef = pd.DataFrame(coeficientes) 
print(df_coef)
print(" ")
print("Agora você pode usar os coeficientes na equação de Steinhart - Hart \npara calcular temperaturas a partir de valores de resistência e analisar o comportamento da temperatura em uma barra metálica, por exemplo  \n1/T = A + B * ln(R) + C * ln(R)^3")
print(" ")

# LOAD
with pd.ExcelWriter(
    "GitHub\\DesafioETL\\calibracao_sensores.xlsx",
    engine="openpyxl",
    mode="a",
    if_sheet_exists="replace"
) as writer:
    df_coef.to_excel(writer, sheet_name="Coeficientes", index=False)
