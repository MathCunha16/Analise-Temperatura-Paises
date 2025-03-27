import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/average-monthly-surface-temperature.csv")

# print(df.info())

pais = ["Tunisia"]
df_filtrado = df[df["Entity"].isin(pais)]

# Filtrando dado do pais
dados_tunisia = df[df["Entity"] == "Tunisia"]

# importando metódo de gerar histograma
from FuncoesGraficas import gerar_histogramas

# gerando histograma da Tunisia
gerar_histogramas("Tunisia", dados_tunisia)  # !!!contem outliers!!!

# importando metódo de identificar outliers
from FuncoesGraficas import identificar_outliers

# selecionando a coluna de temperatura diaria e mensal da Tunisia
coluna_temperatura_diaria = dados_tunisia["Average surface temperature daily"]
coluna_temperatura_mensal = dados_tunisia["Average surface temperature monthly"]

# aplicando a função para identificar outliers
outliers_diaria = identificar_outliers(coluna_temperatura_diaria)
outliers_mensal = identificar_outliers(coluna_temperatura_mensal)

# vendo os outliers
print(f"\nOutliers - Temperaturas (°C):")
print(f"Diários: {outliers_diaria.values.tolist()}")
print(f"Mensais: {outliers_mensal.values.tolist()}\n")

# importando metódo de gerar boxplot
from FuncoesGraficas import gerar_boxplot

# boxplot da Tunisia
gerar_boxplot("Tunisia", dados_tunisia)

# importando metódo de remover outliers
from FuncoesGraficas import remover_outliers

# removendo outliers
temperatura_diaria_limpa = remover_outliers(coluna_temperatura_diaria)
temperatura_mensal_limpa = remover_outliers(coluna_temperatura_mensal)

# criando um dataframe com os dados limpos
dados_tunisia_limpos = pd.DataFrame({
    "Entity": "Tunisia",
    "Average surface temperature daily": temperatura_diaria_limpa,
    "Average surface temperature monthly": temperatura_mensal_limpa
})

# gerando histograma da Tunisia sem outliers
gerar_histogramas("Tunisia (Sem Outliers)", dados_tunisia_limpos)
