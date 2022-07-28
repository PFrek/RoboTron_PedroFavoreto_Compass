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


# Função main
def main():
    # Entrada
    x = int(input())
    
    # Se a entrada for menor ou igual a 2
    if x <= 2:
        # Saída de entrada inválida
        print("Entrada inválida: número deve ser maior que 2")
        return
    
    # Range com os ímpares até X (exclusivo)
    impares = range(1, x, 2)
    
    # Lista com os ímpares até X (inclusivo)
    # impares = range(1, x+1, 2)
    
    # Saída
    for n in impares:
        print(n, end=' ')
        
    print()

if __name__ == '__main__':
    main()