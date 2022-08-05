"""Exercício 8 [20/28]

Enunciado:
    Abra o arquivo CSV com Pandas e guarde em uma variável de sua escolha
    e printe o conteúdo no terminal.

Autor:
    Pedro Favoreto Gaya - 02/08/2022
    
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
