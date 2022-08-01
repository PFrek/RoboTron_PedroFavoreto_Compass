"""Exercício 3 [15/28]

Enunciado:
    Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo
    dentro de variáveis e mostre-as.

Autor:
    Pedro Favoreto Gaya - 01/08/2022
"""

from helper_formatacao import print_header

from exercicio_01 import abrir_json # função abrir_json() do exercicio_01

# Função main
def main():
    # Leitura do arquivo json
    partida_json = abrir_json("dados/partida.json")
    dados_partida = partida_json["copa-do-brasil"][0]
    
    # Obter as informações do json
    nome_estadio = dados_partida["estadio"]["nome_popular"]
    placar = dados_partida["placar"]
    status = dados_partida["status"]
    
    # Saída
    print_header("SAÍDA")
    
    print("Nome do estádio:", nome_estadio)
    print("Placar:", placar)
    print("Status:", status)


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
Nome do estádio: Bruno José Daniel
Placar: Santo André 4x1 Criciuma
Status: finalizado

========================================================================
""" 