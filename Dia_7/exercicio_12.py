"""Exercício 12 [24/28]

Enunciado:
    Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

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
    
    # Series com o nome dos atores dos anos 1991 e 2016
    atores = oscar_df.loc[
        (oscar_df["Year"] == 1991) | (oscar_df["Year"] == 2016), # Linhas
        "Name" # Coluna
    ]


    # Saída
    print_header("SAÍDA")
    
    print("Ator que ganhou o oscar em 1991:", atores.iloc[0])
    print("Ator que ganhou o Oscar em 2016:", atores.iloc[1])

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
Ator que ganhou o Oscar em 1991: Jeremy Irons
Ator que ganhou o Oscar em 2016: Leonardo DiCaprio

========================================================================
""" 
