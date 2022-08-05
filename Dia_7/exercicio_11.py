"""Exercício 11 [23/28]

Enunciado:
    Printe o nome do Ator que ganhou o Oscar em 1993.

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
