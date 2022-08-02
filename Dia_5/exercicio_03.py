"""Exercício 3 [03/28]

Enunciado:
    Construa um programa que recebe dois valores, soma esses valores e
    apresenta se o resultado é par ou ímpar.

Autor:
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
    

    # Entrada dos valores
    print_header("ENTRADA")

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
    print_header("SAÍDA")   
    
    print(f"{valor_1} + {valor_2} = {soma} --> {par_ou_impar}")

if __name__ == '__main__':
    main()

    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
5 3
------------------------------------------------------------------------
[Saída esperada]
5 + 3 = 8 --> PAR

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
2 5
------------------------------------------------------------------------
[Saída esperada]
2 + 5 = 7 --> ÍMPAR

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
1 cinco
------------------------------------------------------------------------
[Saída esperada]
Erro: Entrada inválida. -- (informações do erro)

========================================================================
"""