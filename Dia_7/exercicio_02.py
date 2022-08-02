"""Exercício 2 [14/28]

Enunciado:
    Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.

Autor:
    Pedro Favoreto Gaya - 01/08/2022
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

def obter_time_vencedor(dados_partida):
    """Retorna o nome do time vencedor da partida.

    Args:
        dados_partida (dict): Dicionário contendo as informações da partida.

    Returns:
        str: Nome do time vencedor. Se for um empate, retorna a palavra "Empate"
    """
    # Nome do time mandante
    nome_mandante = dados_partida["time_mandante"]["nome_popular"]
    # Placar do time mandante
    placar_mandante = dados_partida["placar_mandante"]
    
    # Nome do time visitante
    nome_visitante = dados_partida["time_visitante"]["nome_popular"]
    # Placar do time visitante
    placar_visitante = dados_partida["placar_visitante"
                                     ]
    # Se o placar do mandante for maior
    if placar_mandante > placar_visitante:
        # Retorna nome do mandante
        return nome_mandante
        
    # Se o placar do visitante for maior
    elif placar_visitante > placar_mandante:
        # Retorna nome do visitante
        return nome_visitante
    
    # Se os placares forem iguais
    else:
        # Retorna a palavra "Empate"
        return "Empate"

# Função main
def main():
    # Leitura do arquivo json
    partida_json = abrir_json("dados/partida.json")
    dados_partida = partida_json["copa-do-brasil"][0]
    
    # Procura o nome do time vencedor
    vencedor = obter_time_vencedor(dados_partida)
    
    # Saída
    print_header("SAÍDA")
    
    print("Time vencedor:", vencedor)


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
Time vencedor: Santo André

========================================================================
""" 