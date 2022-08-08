"""Exercício 13 [25/28]

Enunciado:
    Crie mais uma coluna em tempo de execução juntando 
    os dados movie e year.

Autor:
    Pedro Favoreto Gaya - 03/08/2022
    
Referências:
    Conversão de colunas numéricas em string para combinação:
    https://datatofish.com/concatenate-values-python/
    
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
    
    # Criar a nova columa juntando "Movie" e "Year"
    oscar_df["Movie+Year"] = oscar_df["Movie"] + " (" + oscar_df["Year"].map(str) + ")"

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
(DataFrame com coluna Movie+Year ao final)

========================================================================
""" 
