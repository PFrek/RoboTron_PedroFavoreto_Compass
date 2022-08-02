"""Exercício 10 [22/28]

Enunciado:
    Usando Pandas, procure por um dado específico (da sua escolha)
    e printe somente o mesmo utilizando o CSV.
    
    Dado procurado: Filme referente ao ano de 1993.

Autor:
    Pedro Favoreto Gaya - 02/08/2022
    
Referências:
    Exibir resultado sem coluna de índice:
    https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index
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
    
    # Objetivo: Nome do filme que ganhou o oscar em 1993
    filme_1993 = oscar_df[oscar_df["Year"] == 1993]["Movie"]
    
    # Saída
    print_header("SAÍDA")
    
    print("Filme referente ao ano de 1993:", filme_1993.to_string(index=False))


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
Filme referente ao ano de 1993: Scent of a Woman

========================================================================
""" 
