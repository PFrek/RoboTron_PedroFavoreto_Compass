"""Exercício 5 [17/28]

Enunciado:
    Guarde o arquivo JSON 2 nomeando-o campeonato em uma variável
    e printe todos os seus dados.

Autor:
    Pedro Favoreto Gaya - 02/08/2022
"""

###
# Importar funções auxiliares do diretório acima
# Referência: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Auxiliar.helper_formatacao import print_header, print_json
###

from exercicio_01 import abrir_json # função abrir_json() do exercicio_01

# Função main
def main():
    # Leitura do arquivo json
    campeonato = abrir_json("dados/campeonato.json")
    
    # Saída
    print_header("SAÍDA")
    
    # Função auxiliar definida em ..\Auxiliar\helper_formatacao.py
    print_json(campeonato)



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
(Conteúdo do arquivo "campeonato.json")

========================================================================
""" 
