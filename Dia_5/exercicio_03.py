"""Exercício 3 [03/28]

Enunciado:
    Construa um programa que recebe dois valores, soma esses valores e
    apresenta se o resultado é par ou ímpar.

Autor:
    Pedro Favoreto Gaya - 27/07/2022
"""

# Função main
def main():
    # Entrada dos valores
    try:
        valor_1, valor_2 = map(int, input("Digite os dois valores inteiros: ").split())
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    # Soma dos valores
    soma = valor_1 + valor_2
    
    # String que indicará se a soma é par ou ímpar
    par_ou_impar = ""
    
    # Se a soma dos valores for par
    if soma % 2 == 0:
        par_ou_impar = "PAR"
       
    # Se não, será ímpar
    else:
        par_ou_impar = "ÍMPAR"

    # Saída
    print(f"{valor_1} + {valor_2} = {soma} --> {par_ou_impar}")

if __name__ == '__main__':
    main()