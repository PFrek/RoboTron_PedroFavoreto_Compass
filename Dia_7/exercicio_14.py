"""Exercício 14 [26/28]

Enunciado:
    Printe todos os nomes e as idades dos atores que ganharam o Oscar
    de 1987 até 1999.

Autor:
    Pedro Favoreto Gaya - 03/08/2022
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
    # Leitura do arquivo csv
    oscar_df = pd.read_csv("dados/oscar.csv", encoding="UTF-8", sep=",")
    
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
