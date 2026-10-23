# Miniprojeto_Erenice_Analise_T9 - Análise Exploratória Varejo

Objetivo: preparar a base Varejo para análises avançadas e dashboard.
Base usada: Base Varejo.csv (830.000 registros)

## O que o script faz
- Carrega a base com pandas e mostra registros, colunas e tipos
- Verifica problemas: nulos por coluna, duplicatas e datas inválidas
- Limpeza mínima: remove nulos de DATA (justificativa: data essencial), remove duplicatas, converte DATA para datetime
- Estatística descritiva da coluna CL_FHL (nº de filhos): média, mediana, desvio, moda, max, min, contagem e quartis
- Agrupamentos: vendas por gênero (CL_GENERO) e por categoria (PR_CAT) usando groupby()
- Gera conclusões e salva Base Varejo_limpa.csv

## Como executar
1. Coloque o arquivo `Base Varejo.csv` na pasta `dados/`
2. Instale: `pip install pandas`
3. Rode: `python limpeza.py`

## Tecnologias
Python, pandas, pathlib

## Autora
Erenice - Turma Analise_T9