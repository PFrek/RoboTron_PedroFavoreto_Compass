"""Exercício 4 [16/28]

Enunciado:
    No JSON 1 printe todas as chaves e valores do time visitante.

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

# Função main
def main():
    # Leitura do arquivo json
    partida_json = abrir_json("dados/partida.json")
    dados_partida = partida_json["copa-do-brasil"][0]
    
    # Dados do time visitante
    time_visitante = dados_partida["time_visitante"]
    
    
    print_header("SAÍDA")
    
    # Para cada par de chave, valor
    for chave, valor in time_visitante.items():
        # Saída do par
        print(f"{chave}: {valor}")


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
time_id: 1
nome_popular: Criciúma
sigla: CRI
escudo: https://apifutebol.s3.sa-east-1.amazonaws.com/escudos/5f999b7c65f34.svg

========================================================================
""" 