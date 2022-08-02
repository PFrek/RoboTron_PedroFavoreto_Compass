"""Exercício 6 [18/28]
s
Enunciado:
    Faça com que o programa printe apenas os primeiros dados
    dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

Autor:
    Pedro Favoreto Gaya - 02/08/2022
    
Referências:
    Sobre a ordenação de dicionários em Python 3.7+:
    https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6

    Obtendo a primeira chave de um dicionário:
    https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
    
Obs.:
    Implementação exige Python versão 3.7 ou acima, pois espera que
    dicionários sejam ordenados por ordem de inserção.
"""

###
# Importar funções auxiliares do diretório acima
# Referência: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Auxiliar.helper_formatacao import print_header
###

from exercicio_01 import abrir_json # função abrir_json() do exercicio_01

# Função main
def main():
    # Leitura do arquivo json
    campeonato = abrir_json("dados/campeonato.json")
    
    # Primeiro dado de edicao_atual
    edicao_primeira_chave = list(campeonato["edicao_atual"])[0]
    edicao_primeiro_valor = campeonato["edicao_atual"][edicao_primeira_chave]
    
    # Primeiro dado de fase_atual
    fase_primeira_chave = list(campeonato["fase_atual"])[0]
    fase_primeiro_valor = campeonato["fase_atual"][fase_primeira_chave]
    
    # Primeiro dado de rodada_atual
    rodada_primeira_chave = list(campeonato["rodada_atual"])[0]
    rodada_primeiro_valor = campeonato["rodada_atual"][rodada_primeira_chave]
    
    # Saída
    print_header("SAÍDA")
    
    print("Primeiro dado de edicao_atual:")
    print(f'"{edicao_primeira_chave}": {edicao_primeiro_valor}')
    
    print()
    print("Primeiro dado de fase_atual:")
    print(f'"{fase_primeira_chave}": {fase_primeiro_valor}')
    
    print()
    print("Primeiro dado de rodada_atual")
    print(f'"{rodada_primeira_chave}": {rodada_primeiro_valor}')

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
Primeiro dado dentro de edicao_atual:
"edicao_id": 20

Primeiro dado dentro de fase_atual:
"fase_id": 104

Primeiro dado dentro de rodada_atual:
"nome": "1ª Rodada"

========================================================================
""" 
