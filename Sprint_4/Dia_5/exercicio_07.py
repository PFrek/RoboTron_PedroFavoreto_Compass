"""Exercício 7 [07/28]

Enunciado:
    Crie um programa que contém uma função que receba 
    dois parâmetros inteiros e retorna a média dos dois valores.

Autor:
    Pedro Favoreto Gaya - 28/07/2022
"""

###
# Importar funções auxiliares do diretório acima
# Referência: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Auxiliar.helper_formatacao import print_header
###


def media(valor_1, valor_2):
    """Retorna a média aritmética de dois inteiros.

    Args:
        valor_1 (int): Primeiro valor.
        valor_2 (int): Segundo valor.

    Returns:
        float: A média aritmética dos dois valores.
    """
    return (valor_1 + valor_2) / 2
    

# Função main
def main():
    
    # Entrada dos dois valores
    print_header("ENTRADA")
    
    try:
        x, y = map(int, input("Digite dois números inteiros: ").split())
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    
    # Saída
    print_header("SAÍDA")
    
    print("Média:", media(x, y))


if __name__ == '__main__':
    main()

    
"""
========================================================================
TEST CASES
========================================================================

Conferência da média feita no site:
https://miniwebtool.com/br/mean-calculator/

========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
1 3
------------------------------------------------------------------------
[Saída esperada]
Média: 2.0

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
-2 8
------------------------------------------------------------------------
[Saída esperada]
Média: 3.0

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
9 26
------------------------------------------------------------------------
[Saída esperada]
Média: 17.5

========================================================================

TC-04:
------------------------------------------------------------------------
[Entrada]
9 2.5
------------------------------------------------------------------------
[Saída esperada]
Erro: Entrada inválida. -- (informações do erro)

========================================================================
""" 