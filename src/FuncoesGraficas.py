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

def analisar_periodo(dataframe, coluna_data):
   
    # convertendo a coluna de data para datetime
    dataframe['data_datetime'] = pd.to_datetime(dataframe[coluna_data])
    
    # extraindo ano e mês
    dataframe['ano_mes'] = dataframe['data_datetime'].dt.to_period('M')
    
    # encontrando o primeiro e o ultimo mês
    primeiro_mes = dataframe['ano_mes'].min()
    ultimo_mes = dataframe['ano_mes'].max()
    
    # imprimindo informações sobre o período
    print(f"\nPeríodo de análise:")
    print(f"Primeiro mês: {primeiro_mes}")
    print(f"Último mês: {ultimo_mes}")
    
    return primeiro_mes, ultimo_mes

def identificar_meses_faltantes(dataframe, coluna_data):
    primeiro_mes = dataframe['ano_mes'].min()
    ultimo_mes = dataframe['ano_mes'].max()
    
    todos_os_meses_esperados = pd.period_range(start=primeiro_mes, end=ultimo_mes, freq='M')
    
    meses_existentes = set(dataframe['ano_mes'].unique())
    
    meses_faltantes = todos_os_meses_esperados.difference(meses_existentes)
    
    if not meses_faltantes.empty:
        print(f"\nMeses faltantes: {len(meses_faltantes)}")
        for mes in meses_faltantes:
            print(f"- {mes}")
    else:
        print("\nNão há meses faltantes no conjunto de dados!")
    
    return meses_faltantes    

def interpolar_dados(dataframe):

    dataframe['Average surface temperature daily'] = dataframe['Average surface temperature daily'].interpolate(method='linear')
    dataframe['Average surface temperature monthly'] = dataframe['Average surface temperature monthly'].interpolate(method='linear')
    
    return dataframe

def gerar_histogramas_interpolados(pais, dados_pais):
    
    plt.figure(figsize=(12, 6))

    # Histograma temperatura diária
    plt.subplot(1, 2, 1)
    plt.hist(
        dados_pais["Average surface temperature daily"],
        bins=30,
        color="blue",
        edgecolor="black",
    )
    plt.title(f"Média Diária Interpolada - {pais}")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequência")

    # Histograma temperatura mensal
    plt.subplot(1, 2, 2)
    plt.hist(
        dados_pais["Average surface temperature monthly"],
        bins=30,
        color="red",
        edgecolor="black",
    )
    plt.title(f"Média Mensal Interpolada - {pais}")
    plt.xlabel("Temperatura (°C)")

    plt.tight_layout()
    plt.show()