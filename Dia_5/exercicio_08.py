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
    try:
        x = int(input("Digite um número inteiro: "))
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
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