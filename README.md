# Análise de Temperatura por País

Este projeto em Python analisa dados de temperatura superficial de diferentes países (Tunisia, Venezuela, Yemen), identificando e tratando outliers nos dados.

## Autor
- [Matheus Cunha Prado](https://github.com/MathCunha16)

## Estrutura do Projeto

```
AnaliseTemperaturaPaises/
├── src/                    # Arquivos Python
│   ├── FuncoesGraficas.py # Funções compartilhadas para visualização
│   ├── AnaliseTunisia.py  # Análise específica da Tunisia
│   ├── AnaliseVenezuela.py # Análise específica da Venezuela
│   └── AnaliseYemen.py    # Análise específica do Yemen
│
├── data/                   # Arquivos de dados
│   └── average-monthly-surface-temperature.csv
│
├── resultados/            # Pasta para as imagens
│   └── (arquivos de imagem)
│
└── .gitignore
```

## Funcionalidades

- Geração de histogramas para análise de distribuição de temperatura
- Identificação de outliers usando o método IQR
- Geração de boxplots para visualização de outliers
- Limpeza de dados removendo outliers

## Como Executar

1. Primeiro, entre na pasta `src`:
   ```bash
   cd src
   ```

2. Depois, execute o arquivo desejado:
   ```bash
   python AnaliseTunisia.py
   python AnaliseVenezuela.py
   python AnaliseYemen.py
   ```

## Dependências

- pandas
- matplotlib

## Resultados

### Tunisia
1. Histograma com Outliers:
![Histograma Tunisia com Outliers](resultados/tunisia_histograma_com_outliers.png)

2. Boxplot identificando os Outliers:
![Boxplot Tunisia](resultados/tunisia_boxplot.png)

3. Histograma após remoção dos Outliers:
![Histograma Tunisia sem Outliers](resultados/tunisia_histograma_sem_outliers.png)

**Outliers Identificados:**
- Temperatura Diária: [29009.0]
- Temperatura Mensal: [ ]

### Venezuela
1. Histograma (não contém nenhum outlier):
![Histograma Venezuela](resultados/venezuela_histograma.png)

### Yemen
1. Histograma com Outliers:
![Histograma Yemen com Outliers](resultados/yemen_histograma_com_outliers.png)

2. Boxplot identificando os Outliers:
![Boxplot Yemen](resultados/yemen_boxplot.png)

3. Histograma após remoção dos Outliers:
![Histograma Yemen sem Outliers](resultados/yemen_histograma_sem_outliers.png)

**Outliers Identificados:**
- Temperatura Diária: [22715.0]
- Temperatura Mensal: [ ] 
