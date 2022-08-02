"""Exercício 7 [19/28]

Enunciado:
    Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

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

from exercicio_01 import abrir_json

# Função main
def main():
    # Leitura do arquivo json
    campeonato = abrir_json("dados/campeonato.json")
    
    # Saída
    print_header("SAÍDA")
    
    print("Chaves principais de campeonato.json:")
    
    # Para cada chave em campeonato.json
    for chave in campeonato:
        # Imprime a chave
        print(chave)


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
Chaves principais de campeonato.json:
campeonato_id
nome
slug
nome_popular
edicao_atual
fase_atual
rodada_atual
status
tipo
logo
regiao
fases

========================================================================
""" 
