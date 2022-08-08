"""Exercício 3 [03/28]

Enunciado:
    Construa um programa que recebe dois valores, soma esses valores e
    apresenta se o resultado é par ou ímpar.

Autor:
    Pedro Favoreto Gaya - 27/07/2022
    
Referências:
    Verificar se um float contém um número inteiro:
    https://note.nkmk.me/en/python-check-int-float/
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
        # Recebe e tenta converter as entradas para float
        valor_1, valor_2 = map(float, input("Digite os dois valores: ").split())
    except ValueError as err:
        # Saída de erro
        print("Erro: Entrada inválida. -- ", err)
        return
    
    # Soma dos valores
    soma = valor_1 + valor_2
    
    # String que indicará se a soma é par, ímpar ou indefinido
    par_ou_impar = ""
    
    # Se a soma não resultar em um número inteiro
    if not soma.is_integer():
        par_ou_impar = "INDEFINIDO"
    
    # Se a soma dos valores for par
    elif soma % 2 == 0:
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

TC-01: (Entrada inteiros, resultado par)
------------------------------------------------------------------------
[Entrada]
5 3
------------------------------------------------------------------------
[Saída esperada]
5.0 + 3.0 = 8.0 --> PAR

========================================================================

TC-02: (Entrada inteiros, resultado ímpar)
------------------------------------------------------------------------
[Entrada]
2 5
------------------------------------------------------------------------
[Saída esperada]
2.0 + 5.0 = 7.0 --> ÍMPAR

========================================================================

TC-03: (Entrada decimal, resultado par)
------------------------------------------------------------------------
[Entrada]
1.2 2.8
------------------------------------------------------------------------
[Saída esperada]
1.2 + 2.8 = 4.0 --> PAR

========================================================================

TC-04: (Entrada decimal, resultado ímpar)
------------------------------------------------------------------------
[Entrada]
1.2 1.8
------------------------------------------------------------------------
[Saída esperada]
1.2 + 1.8 = 3.0 --> ÍMPAR

========================================================================

TC-05: (Entrada decimal, resultado decimal)
------------------------------------------------------------------------
[Entrada]
1.5 1.7
------------------------------------------------------------------------
[Saída esperada]
1.5 + 1.7 = 3.2 --> INDEFINIDO

========================================================================

TC-06: (Entrada inválida)
------------------------------------------------------------------------
[Entrada]
1 cinco
------------------------------------------------------------------------
[Saída esperada]
Erro: Entrada inválida. -- (informações do erro)

========================================================================
"""