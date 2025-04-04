import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/average-monthly-surface-temperature.csv")

pais = ["Venezuela"]
df_filtrado = df[df["Entity"].isin(pais)]

# Filtrando dado do pais
dados_venezuela = df[df["Entity"] == "Venezuela"]

# importando metódo de gerar histograma
from FuncoesGraficas import gerar_histogramas

# gerando histograma da Venezuela
gerar_histogramas("Venezuela", dados_venezuela)  # !!! não contem outlier aparente !!!

# importando metódo de identificar outliers
from FuncoesGraficas import identificar_outliers

# selecionando a coluna de temperatura diaria e mensal da Venezuela
coluna_temperatura_diaria = dados_venezuela["Average surface temperature daily"]
coluna_temperatura_mensal = dados_venezuela["Average surface temperature monthly"]

# aplicando a função para identificar outliers
outliers_diaria = identificar_outliers(coluna_temperatura_diaria)
outliers_mensal = identificar_outliers(coluna_temperatura_mensal)

# vendo os outliers
print(f"\nOutliers - Temperaturas (°C):")
print(f"Diários: {outliers_diaria.values.tolist()}")
print(f"Mensais: {outliers_mensal.values.tolist()}\n")

# Os outliers apontados não me parecem ser de fato outliers, pois não estão muito longe da media, ent
# n vou remover eles

# -----------------------------------
# Parte 2: completamento de dados
# -----------------------------------

from FuncoesGraficas import analisar_periodo # importando função de analisar periodo

mes_inicial, mes_final = analisar_periodo(dados_venezuela, "Day")

print("-" * 100)

from FuncoesGraficas import identificar_meses_faltantes # importando função de identificar meses faltantes

identificar_meses_faltantes(dados_venezuela, "Day") 

# A venezuela não apresenta meses faltantes, então novamente, não irei realizar nenhum tipo de tratamento de dados
# também não to tratando o alerta de SettingWithCopyWarning, visto que a professora também não tratou

