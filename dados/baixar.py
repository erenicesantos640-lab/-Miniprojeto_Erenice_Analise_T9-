import kagglehub
import shutil
import os
from pathlib import Path

# 1. Baixa o dataset (vai pro cache)
print("Baixando dataset...")
cache_path = kagglehub.dataset_download("namespaiva/base-varejo")
print(f"Baixado no cache: {cache_path}")

# 2. Define onde é a sua pasta 'dados'
# A pasta dados é a pasta onde este arquivo baixar.py está
pasta_destino = Path(__file__).parent
print(f"Sua pasta de destino: {pasta_destino}")

# 3. Copia todos os arquivos do cache pra dentro de 'dados'
for arquivo in Path(cache_path).iterdir():
    if arquivo.is_file():
        destino = pasta_destino / arquivo.name
        print(f"Copiando {arquivo.name} -> {destino}")
        shutil.copy2(arquivo, destino)

print("\nPronto! Arquivos na sua pasta dados:")
for f in pasta_destino.iterdir():
    print(f" - {f.name}")