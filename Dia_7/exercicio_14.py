"""Exercício 14 [26/28]

Enunciado:
    Printe todos os nomes e as idades dos atores que ganharam o Oscar
    de 1987 até 1999.

Autor:
    Pedro Favoreto Gaya - 03/08/2022

Referências:
    Correção do caminho relativo do arquivo:
    https://stackoverflow.com/questions/918154/relative-paths-in-python
"""

###
# Importar funções auxiliares do diretório acima
# Referência: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Auxiliar.helper_formatacao import print_header
###

import pandas as pd

# Função main
def main():
    # Leitura do arquivo CSV
    try:
        # Montagem do caminho absoluto para o arquivo.
        # Permite executar o script a partir de outras pastas, sem que haja erro.
        diretorio = os.path.dirname(__file__)
        arquivo_csv = os.path.join(diretorio, "dados/oscar.csv")
        
        oscar_df = pd.read_csv(arquivo_csv, encoding="UTF-8", sep=",")
    except FileNotFoundError as err:
        print("Erro: Arquivo não encontrado --", err)
        return
    
    # DataFrame contendo os nomes e idades dos anos 1987 - 1999
    resultado_df = oscar_df.loc[
        (oscar_df["Year"] >= 1987) & (oscar_df["Year"] <= 1999), # Linhas
        ["Name", "Age"] # Colunas
    ]
    
    # Saída
    print_header("SAÍDA")

    print(resultado_df)

if __name__ == '__main__':
    main()
    

"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
(vazia)
------------------------------------------------------------------------
[Saída esperada]
(DataFrame contendo as colunas Name e Year dos anos 1987-1999)
        Name        Age
Paul Newman         62
Michael Douglas     43
...
Jack Nicholson      60
Roberto Benigni     46

========================================================================
""" 
