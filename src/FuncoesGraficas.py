import pandas as pd
import matplotlib.pyplot as plt

def gerar_histogramas(pais, dados_pais):  # função que gera histogramas

    plt.figure(figsize=(12, 6))

    # histograma temperatura diária
    plt.subplot(1, 2, 1)
    plt.hist(
        dados_pais["Average surface temperature daily"],
        bins=30,
        color="blue",
        edgecolor="black",
    )
    plt.title(f"Média Diária - {pais}")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequência")

    # histograma temperatura mensal
    plt.subplot(1, 2, 2)
    plt.hist(
        dados_pais["Average surface temperature monthly"],
        bins=30,
        color="red",
        edgecolor="black",
    )
    plt.title(f"Média Mensal - {pais}")
    plt.xlabel("Temperatura (°C)")

    plt.tight_layout()
    plt.show()
    
    
def identificar_outliers(coluna):  # função para identificar outliers
    Q1 = coluna.quantile(0.25)
    Q3 = coluna.quantile(0.75)

    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    outliers = coluna[(coluna < limite_inferior) | (coluna > limite_superior)]
    return outliers

def remover_outliers(dados):
    Q1 = dados.quantile(0.25)
    Q3 = dados.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return dados[(dados >= limite_inferior) & (dados <= limite_superior)]

def gerar_boxplot(pais, dados_pais): # função que gera boxplot

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.boxplot(dados_pais["Average surface temperature daily"])
    plt.title(f"Boxplot - Temperatura diária - {pais}")
    plt.xlabel("Temperatura")

    plt.subplot(1, 2, 2)
    plt.boxplot(dados_pais["Average surface temperature monthly"])
    plt.title(f"Boxplot - Temperatura mensal - {pais}")
    plt.xlabel("Temperatura")

    plt.show()    