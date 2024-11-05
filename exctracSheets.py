"""
Extrair tabela que se estende por multiplas páginas de arquivo pdf e exporta-las em formato CSV"""

import tabula
import pandas as pd

pdf_path = r"C:\\Users\\leona\\Documents\\contabeis\\demonstrações brf 2020-2024\\DFP – Demonstrações Financeiras Padronizadas 2021.pdf"

# Ler página inicial
pag_ini = 4
dfs = tabula.read_pdf(pdf_path, pages=pag_ini, lattice=False, encoding='ansi')
mergedDf = pd.concat(dfs)

# Iterar sobre as páginas seguintes e concatenar linhas mantendo a mesma estrutura de colunas
for i in range(2):
    tempDfs = tabula.read_pdf(pdf_path, pages=pag_ini+i, lattice=False, encoding='ansi')
    tempDf = pd.concat(tempDfs).drop(0)
    # Verificar se as colunas estão alinhadas corretamente
    if all(col in mergedDf.columns for col in tempDf.columns):
        mergedDf = pd.concat([mergedDf, tempDf], ignore_index=True)
    else:
        tempDf = tempDf.dropna(axis=1)
        mergedDf = pd.concat([mergedDf, tempDf], ignore_index=True)
        print(f"Colunas não alinhadas na página {5 + i}")



# Excluir colunas irrelevantes
cols_to_drop = [0, 4]
mergedDfTrimed = mergedDf.drop(mergedDf.columns[cols_to_drop], axis=1)
print(mergedDfTrimed)


# Exportar o DataFrame para um arquivo CSV
output_path = r"C:\\Users\\leona\\Documents\\contabeis\\demonstrações brf 2020-2024\\bpBrf2023.csv"
#mergedDfTrimed.to_csv(output_path, index=False)
print(f"DataFrame exportado para CSV com sucesso! Caminho do arquivo: {output_path}")

