"""Exercício 15 [27/28]

Enunciado:
    Mostre todos os filmes menos o "The Revenant".

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
    
    # Series com os filmes, excluindo The Revenant
    filmes = oscar_df.loc[oscar_df["Movie"] != "The Revenant", "Movie"]
    
    
    # Saída
    print_header("SAÍDA")

    print("Filmes, exceto The Revenant: ")
    print(filmes)


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
(Series com os filmes, excluindo The Revenant)

========================================================================
""" 
