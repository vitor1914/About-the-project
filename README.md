
# Identificação de Valores Ausentes | Missing Values Detection

## 🇧🇷 Português

### Sobre o projeto

Projeto de análise de dados desenvolvido em Python para identificar e quantificar valores ausentes em uma base de clientes. A solução utiliza Pandas para processar os dados e Matplotlib para gerar visualizações que auxiliam na avaliação da qualidade da base.

### Objetivos

- Identificar valores ausentes em cada coluna.
- Calcular a quantidade de valores preenchidos e ausentes.
- Calcular o percentual de ausência por coluna.
- Calcular o percentual geral de células ausentes.
- Exportar relatórios nos formatos CSV e JSON.
- Criar gráficos para facilitar a interpretação dos resultados.
- Preservar os dados originais, sem exclusões automáticas.

### Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- CSV
- JSON

### Estrutura do projeto

```text
identificacao-valores-ausentes/
├── dados/
│   └── clientes.csv
├── graficos/
│   ├── valores_ausentes.png
│   └── percentual_valores_ausentes.png
├── relatorios/
│   ├── base_analisada.csv
│   ├── resumo_analise.json
│   └── valores_ausentes_por_coluna.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Funcionalidades

1. Leitura de uma base de dados em CSV.
2. Identificação de células vazias e marcadores comuns de ausência.
3. Cálculo da quantidade e do percentual de valores ausentes por coluna.
4. Cálculo do percentual geral de células ausentes.
5. Exportação de relatórios para análise posterior.
6. Geração de gráficos com a distribuição dos valores ausentes.

### Como executar

Requisitos: Python 3.10 ou superior.

1. Abra a pasta do projeto no terminal.
2. Crie um ambiente virtual:

   `python3 -m venv .venv`

3. Ative o ambiente virtual no Linux:

   `source .venv/bin/activate`

4. Instale as dependências:

   `python -m pip install -r requirements.txt`

5. Execute o programa:

   `python main.py`

### Arquivos de saída

| Arquivo | Descrição |
|---|---|
| `valores_ausentes_por_coluna.csv` | Quantidade e percentual de ausentes por coluna |
| `base_analisada.csv` | Cópia da base utilizada na análise |
| `resumo_analise.json` | Indicadores gerais e detalhamento |
| `valores_ausentes.png` | Gráfico de quantidade de ausentes |
| `percentual_valores_ausentes.png` | Gráfico de percentual de ausentes |

Os relatórios CSV ficam na pasta `relatorios/`, e as visualizações são salvas em `graficos/`.

### Considerações sobre os dados

Valores ausentes podem ocorrer por falhas de preenchimento, coleta incompleta ou indisponibilidade de informações. A identificação é uma etapa importante da análise exploratória de dados.

Este projeto não preenche nem remove valores ausentes automaticamente. O tratamento deve ser escolhido considerando o significado das variáveis e o objetivo da análise.

### Possíveis melhorias

- Comparação entre estratégias de tratamento de dados ausentes.
- Identificação de padrões de ausência.
- Criação de testes automatizados.
- Desenvolvimento de uma interface para carregar diferentes arquivos CSV.
- Integração com um dashboard de qualidade de dados.

---

## 🇺🇸 English

### About the project

A data analysis project built with Python to identify and quantify missing values in a customer dataset. The solution uses Pandas to process data and Matplotlib to create visualizations that support data quality assessment.

### Objectives

- Identify missing values in each column.
- Calculate the number of missing and non-missing values.
- Calculate the missing-value percentage for each column.
- Calculate the overall percentage of missing cells.
- Export reports in CSV and JSON formats.
- Create charts to improve result interpretation.
- Preserve the original data without automatically deleting records.

### Technologies

- Python
- Pandas
- Matplotlib
- CSV
- JSON

### Project structure

```text
identificacao-valores-ausentes/
├── dados/
│   └── clientes.csv
├── graficos/
├── relatorios/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Features

1. Read a CSV dataset.
2. Identify empty cells and common missing-value markers.
3. Calculate missing-value counts and percentages by column.
4. Calculate the overall percentage of missing cells.
5. Export reports for further analysis.
6. Generate charts showing the distribution of missing values.

### How to run

Requirements: Python 3.10 or newer.

1. Open the project folder in a terminal.
2. Create a virtual environment:

   `python3 -m venv .venv`

3. Activate the environment on Linux:

   `source .venv/bin/activate`

4. Install the dependencies:

   `python -m pip install -r requirements.txt`

5. Run the program:

   `python main.py`

### Output files

| File | Description |
|---|---|
| `valores_ausentes_por_coluna.csv` | Missing-value counts and percentages by column |
| `base_analisada.csv` | Copy of the dataset used in the analysis |
| `resumo_analise.json` | Overall indicators and detailed results |
| `valores_ausentes.png` | Chart of missing-value counts |
| `percentual_valores_ausentes.png` | Chart of missing-value percentages |

CSV reports are saved in the `relatorios/` directory, and visualizations are saved in `graficos/`.

### Data considerations

Missing values may result from incomplete data collection, unfilled fields, or unavailable information. Detecting them is an important step in exploratory data analysis.

This project does not automatically fill or remove missing values. Treatment decisions should consider the meaning of each variable and the goals of the analysis.

### Possible improvements

- Compare missing-data treatment strategies.
- Identify missingness patterns.
- Add automated tests.
- Build an interface for uploading different CSV files.
- Integrate with a data quality dashboard.
