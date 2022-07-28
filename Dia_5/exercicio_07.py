"""Exercício 7 [07/28]

Enunciado:
    Crie um programa que contém uma função que receba 
    dois parâmetros inteiros e retorna a média dos dois valores.

Autor:
    Pedro Favoreto Gaya - 28/07/2022
"""

# TODO - Verificação da entrada

def media(valor_1, valor_2):
    """Retorna a média aritmética de dois inteiros.

    Args:
        valor_1 (int): Primeiro valor inteiro.
        valor_2 (int): Segundo valor inteiro.
    """
    return (valor_1 + valor_2) / 2
    


# Função main
def main():
    # Entrada dos dois valores
    try:
        x, y = map(int, input("Digite dois números inteiros: ").split())
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    # Saída
    print("Média:", media(x, y))


if __name__ == '__main__':
    main()