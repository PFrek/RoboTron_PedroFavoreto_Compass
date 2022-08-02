"""Exercício 9 [21/28]

Enunciado:
    Usando Pandas, leia apenas os dados da coluna Age do CSV.

Autor:
    Pedro Favoreto Gaya - 02/08/2022
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
    # Leitura do arquivo CSV, somente coluna Age
    idades_df = pd.read_csv("dados/oscar.csv", encoding="UTF-8", sep=",", usecols=["Age"])
    
    # Saída
    print_header("SAÍDA")
    
    print(idades_df) 


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
(DataFrame contendo a coluna "Age" do arquivo "oscar.csv")

========================================================================
""" 
