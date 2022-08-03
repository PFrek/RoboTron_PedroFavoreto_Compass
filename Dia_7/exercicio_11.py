"""Exercício 11 [23/28]

Enunciado:
    Printe o nome do Ator que ganhou o Oscar em 1993.

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
    
    # Series com o nome do ator do ano 1993
    ator_1993 = oscar_df.loc[
        oscar_df["Year"] == 1993,   # Linha
        "Name"                      # Coluna
    ]
 
    # Saída
    print_header("SAÍDA")
    
    print("Ator que ganhou o Oscar em 1993:", ator_1993.to_string(index=False))


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
Ator que ganhou o Oscar em 1993: Al Pacino

========================================================================
""" 
