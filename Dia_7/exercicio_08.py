"""Exercício 8 [20/28]

Enunciado:
    Abra o arquivo CSV com Pandas e guarde em uma variável de sua escolha
    e printe o conteúdo no terminal.

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
    # Leitura do arquivo CSV
    oscar_df = pd.read_csv("dados/oscar.csv", encoding="UTF-8", sep=",")
    
    # Saída
    print_header("SAÍDA")
    
    print(oscar_df)

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
(Conteúdo do arquivo "oscar.csv")

========================================================================
""" 
