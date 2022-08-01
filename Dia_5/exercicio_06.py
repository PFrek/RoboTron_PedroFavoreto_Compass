"""Exercício 6 [06/28]

Enunciado:
    Construa um programa que receba um valor inteiro maior que 2
    em uma variável x e apresenta os ímpares entre 0 e X.

Autor:
    Pedro Favoreto Gaya - 28/07/2022
    
Referência:
    Python range():
    https://www.w3schools.com/python/ref_func_range.asp
"""

from helper_formatacao import print_header

# Função main
def main():
    
    # Entrada
    print_header("ENTRADA")
    
    try:
        x = int(input("Digite um número inteiro maior ou igual a 2: "))
        
        # Se a entrada for menor que 2
        if x < 2:
            raise ValueError("Número deve ser maior ou igual a 2")
        
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    
    
    # Lista com os ímpares até X (inclusivo)
    impares = range(1, x+1, 2)
    
    
    # Saída
    print_header("SAÍDA")
    
    for n in impares:
        print(n, end=' ')
        
    print()

if __name__ == '__main__':
    main()

    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
1
------------------------------------------------------------------------
[Saída esperada]
Erro: Entrada inválida. -- Número deve ser maior ou igual a 2

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
2
------------------------------------------------------------------------
[Saída esperada]
1

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
8
------------------------------------------------------------------------
[Saída esperada]
1 3 5 7

========================================================================

TC-04:
------------------------------------------------------------------------
[Entrada]
9
------------------------------------------------------------------------
[Saída esperada]
1 3 5 7 9

========================================================================
""" 