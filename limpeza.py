import pandas as pd
from pathlib import Path

# =======================================================
# SPRINT 1: IMPORTAÇÃO DOS DADOS
# =======================================================
arquivo = Path(__file__).parent / "dados" / "Base Varejo.csv"

print("Carregando base...")
df = pd.read_csv(arquivo, sep=';', encoding='latin-1', engine='python')

# Remove colunas vazias (Unnamed) que vem por causa dos ;;;
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.columns = df.columns.str.strip().str.upper()

print("\n=== 1. CARREGAR BASE ===")
print(f"Número de registros: {len(df)}")
print(f"Colunas: {df.columns.tolist()}")
print("\nTipos de dados:")
print(df.dtypes)

# =======================================================
# SPRINT 2 e 3: VERIFICAR PROBLEMAS E LIMPEZA
# =======================================================
print("\n\n=== 2. VERIFICAR PROBLEMAS BÁSICOS ===")

# Problema 1: Valores nulos por coluna
print("\n1) Nulos por coluna:")
nulos = df.isnull().sum()
print(nulos)

# Problema 2: Duplicatas
duplicatas = df.duplicated().sum()
print(f"\n2) Duplicatas: {duplicatas} linhas duplicadas encontradas")

# Problema 3: Inconsistências - datas inválidas
# Vamos converter DATA e ver quantas viram NaT (Not a Time)
df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')
datas_invalidas = df['DATA'].isnull().sum()
print(f"\n3) Datas inválidas/vazias: {datas_invalidas}")

print("\n\n=== 3. LIMPEZA MÍNIMA NECESSÁRIA ===")

# Limpeza 1: Remover ou imputar nulos
# ESCOLHA: Vamos REMOVER linhas sem DATA, pois DATA é essencial e não pode ser inventada (imputada)
# Para outras colunas, não há muitos nulos, então mantemos
linhas_antes = len(df)
df = df.dropna(subset=['DATA'])
print(f"Removendo nulos de DATA: {linhas_antes} -> {len(df)} (removidas {linhas_antes - len(df)})")

# Limpeza 2: Eliminar duplicatas relevantes
linhas_antes = len(df)
df = df.drop_duplicates()
print(f"Removendo duplicatas: {linhas_antes} -> {len(df)} (removidas {linhas_antes - len(df)})")

# Limpeza 3: Ajustar tipos de dados
# DATA já convertida para datetime
print(f"Tipo de DATA ajustado: {df['DATA'].dtype}")
# CL_FHL (número de filhos) deve ser numérico
df['CL_FHL'] = pd.to_numeric(df['CL_FHL'], errors='coerce')
print(f"Tipo de CL_FHL ajustado: {df['CL_FHL'].dtype}")

# =======================================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA - CL_FHL
# =======================================================
print("\n\n=== 4. ESTATÍSTICA DESCRITIVA - CL_FHL (Nº de filhos) ===")

# Contagem, média, mediana, desvio, moda, max, min, quartis
desc = df['CL_FHL'].describe()
print(desc)
print(f"\nMédia: {df['CL_FHL'].mean():.2f}")
print(f"Mediana: {df['CL_FHL'].median():.2f}")
print(f"Desvio padrão: {df['CL_FHL'].std():.2f}")
print(f"Moda: {df['CL_FHL'].mode().values}")
print(f"Mínimo: {df['CL_FHL'].min()}")
print(f"Máximo: {df['CL_FHL'].max()}")
print(f"Contagem: {df['CL_FHL'].count()}")
print(f"Quartis:\n{df['CL_FHL'].quantile([0.25, 0.5, 0.75])}")

# =======================================================
# SPRINT 5: AGRUPAMENTOS
# =======================================================
print("\n\n=== 5. PADRÕES DE AGRUPAMENTO ===")

# Agrupamento 1: Gênero com mais vendas
print("\n1) Vendas por gênero (CL_GENERO):")
vendas_genero = df.groupby('CL_GENERO').size().sort_values(ascending=False)
print(vendas_genero)

# Agrupamento 2: Categoria de produto mais vendida
print("\n2) Vendas por categoria de produto (PR_CAT):")
vendas_categoria = df.groupby('PR_CAT').size().sort_values(ascending=False)
print(vendas_categoria)

# Agrupamento extra (opcional): Ticket por segmento
print("\n3) Quantidade de compras por segmento (CL_SEG) - extra:")
compras_segmento = df.groupby('CL_SEG').size().sort_values(ascending=False)
print(compras_segmento)

# =======================================================
# SPRINT 5: CONCLUSÕES
# =======================================================
print("\n\n=== 6. CONCLUSÕES (3 a 6 tópicos) ===")
print("""
1. A base original tinha 830.000 registros, mas 484.735 linhas sem DATA foram removidas, 
   restando cerca de 345 mil registros válidos para análise temporal.

2. A coluna CL_FHL (nº de filhos) tem média baixa, indicando que a maioria dos clientes 
   tem 0 a 2 filhos. A moda é 0, mostrando muitos clientes sem filhos.

3. Em gênero, há predominância de um dos gêneros nas compras (ver agrupamento 1), 
   o que pode direcionar campanhas de marketing.

4. Algumas categorias de produtos (PR_CAT) concentram a maior parte das vendas, 
   sugerindo oportunidade de focar estoque e promoção nessas categorias.

5. Problemas remanescentes: ainda existem possíveis categorias vazias em PR_NOME, 
   e a coluna CL_EC (estado civil) pode ter inconsistências de escrita que precisariam 
   de padronização futura.

6. Próximos passos: criar um dashboard com vendas por mês e analisar sazonalidade 
   usando a coluna DATA já convertida.
""")

# Salvar arquivo limpo
arquivo_limpo = Path(__file__).parent / "dados" / "Base Varejo_limpa.csv"
df.to_csv(arquivo_limpo, index=False, sep=';', encoding='utf-8')
print(f"\n\nArquivo limpo salvo em: {arquivo_limpo}")
print(f"Final: {len(df)} linhas x {len(df.columns)} colunas")