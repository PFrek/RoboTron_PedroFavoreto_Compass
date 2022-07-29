"""Exercício 7 [07/28]

Enunciado:
    Crie um programa que contém uma função que receba 
    dois parâmetros inteiros e retorna a média dos dois valores.

Autor:
    Pedro Favoreto Gaya - 28/07/2022
"""


def media(valor_1, valor_2):
    """Retorna a média aritmética de dois inteiros.

    Args:
        valor_1 (int): Primeiro valor inteiro.
        valor_2 (int): Segundo valor inteiro.
    """
    return (valor_1 + valor_2) / 2
    


# Função main
def main():
    
    print("="*30)
    print("ENTRADA")
    print("="*30)
    
    # Entrada dos dois valores
    try:
        x, y = map(int, input("Digite dois números inteiros: ").split())
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    print("="*30)
    print("SAÍDA")
    print("="*30)
    
    # Saída
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
2

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
-2 8
------------------------------------------------------------------------
[Saída esperada]
3

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
9 26
------------------------------------------------------------------------
[Saída esperada]
17.5

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