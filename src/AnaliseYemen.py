import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/average-monthly-surface-temperature.csv")

pais = ["Yemen"]
df_filtrado = df[df["Entity"].isin(pais)]

# Filtrando dado do pais
dados_yemen = df[df["Entity"] == "Yemen"]

# importando metódo de gerar histograma
from FuncoesGraficas import gerar_histogramas

# gerando histograma do Yemen
gerar_histogramas("Yemen", dados_yemen)  # !!!contem outliers!!!

# importando metódo de identificar outliers
from FuncoesGraficas import identificar_outliers

# selecionando a coluna de temperatura diaria e mensal do Yemen
coluna_temperatura_diaria = dados_yemen["Average surface temperature daily"]
coluna_temperatura_mensal = dados_yemen["Average surface temperature monthly"]

# aplicando a função para identificar outliers
outliers_diaria = identificar_outliers(coluna_temperatura_diaria)
outliers_mensal = identificar_outliers(coluna_temperatura_mensal)

# vendo os outliers
print(f"\nOutliers - Temperaturas (°C):")
print(f"Diários: {outliers_diaria.values.tolist()}")  # Outlier encontrado !!!
print(f"Mensais: {outliers_mensal.values.tolist()}\n")

# importando metódo de gerar boxplot
from FuncoesGraficas import gerar_boxplot

# boxplot do Yemen
gerar_boxplot("Yemen", dados_yemen)

# importando metódo de remover outliers
from FuncoesGraficas import remover_outliers

# removendo outliers
temperatura_diaria_limpa = remover_outliers(coluna_temperatura_diaria)
temperatura_mensal_limpa = remover_outliers(coluna_temperatura_mensal)

# criando um dataframe com os dados limpos
dados_yemen_limpos = pd.DataFrame({
    "Entity": "Yemen",
    "Average surface temperature daily": temperatura_diaria_limpa,
    "Average surface temperature monthly": temperatura_mensal_limpa
})

# gerando histograma do Yemen sem outliers
gerar_histogramas("Yemen (Sem Outliers)", dados_yemen_limpos)
