"""Exercício 8 [08/28]

Enunciado:
    Crie um programa que lê 1 valor inteiro para X. 
    Se o valor for par, calcular o fatorial de X em uma função e apresentar
    o resultado fora da função.
    Se o valor for ímpar, apresentar em uma função a tabuada de 1 a 10 de X.

Autor:
    Pedro Favoreto Gaya - 28/07/2022
    
Referência:
    Comportamento para 0!
    https://pt.wikipedia.org/wiki/Fatorial
"""

from helper_formatacao import print_header


def fatorial(x):
    """Calcula o fatorial de X (X!) por meio de recursão.

    Args:
        x (int): Valor inteiro para cálculo do fatorial.

    Raises:
        ValueError: Erro gerado no caso da entrada de número negativo.

    Returns:
        int: O fatorial de X (X!).
    """
    
    # Se x for negativo, gerar erro
    if x < 0:
        raise ValueError("Função fatorial é indefinida para números negativos")
    
    # Por convenção, 0! == 1
    # Caso base, X == 1
    if x == 0 or x == 1:
        return 1

    # Loop recursivo
    else:
        return x * fatorial(x-1)
    

def tabuada(x):
    """Apresenta a tabuada de 1 a 10 de X.

    Args:
        x (int): Valor do qual a tabuada será apresentada.
    """
    
    # Para cada número entre 1 e 10
    for i in range(1, 11):
        # Saída da tabuada de X
        print(f"{i} x {x} = {i*x}")

# Função main
def main():
    
    # Entrada do inteiro X
    print_header("ENTRADA")
    
    try:
        x = int(input("Digite um número inteiro: "))
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    

    print_header("SAÍDA")
    
    # Se X for par
    if x % 2 == 0:
        try:        
            # Calcular o fatorial de X
            x_fatorial = fatorial(x)
        except ValueError as err:
            print("Erro: Entrada inválida. -- ", err)
            return
        
        # Saída
        print(f"{x}! = {x_fatorial}")
        
    # Caso contrário, se for ímpar
    else:
        # Apresentar a tabuada de X
        tabuada(x)
        

if __name__ == '__main__':
    main()
  
    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
6
------------------------------------------------------------------------
[Saída esperada]
6! = 720

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
5
------------------------------------------------------------------------
[Saída esperada]
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
-4
------------------------------------------------------------------------
[Saída esperada]
Erro: Entrada inválida. -- Função fatorial é indefinida para números negativos

========================================================================

TC-04:
------------------------------------------------------------------------
[Entrada]
-9
------------------------------------------------------------------------
[Saída esperada]
1 x -9 = -9
2 x -9 = -18
3 x -9 = -27
4 x -9 = -36
5 x -9 = -45
6 x -9 = -54
7 x -9 = -63
8 x -9 = -72
9 x -9 = -81
10 x -9 = -90

========================================================================
""" 