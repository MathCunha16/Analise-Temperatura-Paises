import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/average-monthly-surface-temperature.csv")

# <---- debug ---->
# pd.set_option('display.max_rows', None) 
# print(df.info())
#print(df.columns)
# <---- debug ---->

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

print("-" * 100)

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
    "Day": dados_tunisia["Day"],  # !!! incluindo essa coluna pra usar na proxima parte do codigo !!!!
    "Average surface temperature daily": temperatura_diaria_limpa,
    "Average surface temperature monthly": temperatura_mensal_limpa
})

# gerando histograma da Tunisia sem outliers
gerar_histogramas("Tunisia (Sem Outliers)", dados_tunisia_limpos)

# -----------------------------------
# Parte 2: completamento de dados
# -----------------------------------

# importando metódo de analisar periodo
from FuncoesGraficas import analisar_periodo

mes_inicial, mes_final = analisar_periodo(dados_tunisia_limpos, "Day") # analisando o periodo de dados

print("-" * 100)

from FuncoesGraficas import identificar_meses_faltantes # importando função de identificar meses faltantes

identificar_meses_faltantes(dados_tunisia_limpos, "Day")
  
print("-" * 100)  

from FuncoesGraficas import interpolar_dados # importando função de interpolar dados

dados_tunisia_limpos = interpolar_dados(dados_tunisia_limpos)

from FuncoesGraficas import gerar_histogramas_interpolados # importando função de gerar histogramas interpolados

gerar_histogramas_interpolados("Tunisia (Com Interpolacao)", dados_tunisia_limpos)