"""Exercício 2 [02/28]

Enunciado:
    Construa um programa que armazena em duas variáveis duas notas e apresenta
    a média entre as duas.

Autor:py
    Pedro Favoreto Gaya - 27/07/2022
"""

###
# Importar funções auxiliares do diretório acima
# Referência: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Auxiliar.helper_formatacao import print_header
###


# Função main
def main():
    # Inicialização das variáveis
    nota_1 = 9
    nota_2 = 8.5
    
    # Cálculo da média
    media = (nota_1 + nota_2) / 2
    
    # Saída
    print_header("SAÍDA")
    
    print("Média:", media)


if __name__ == '__main__':
    main()


"""
========================================================================
TEST CASES
========================================================================

Site para teste:
https://miniwebtool.com/br/mean-calculator/

========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
(vazia)
------------------------------------------------------------------------
[Saída esperada]
Média: 8.75

========================================================================
"""