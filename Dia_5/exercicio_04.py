"""Exercício 4 [04/28]

Enunciado:
    Construa um programa que armazena uma idade em uma variável e compara,
    se a idade for maior que 18, apresenta "Maior de idade",
    se a idade for menor que 12, apresenta "Você é uma criança"
    e se for maior que 12 e menor que 18, apresenta "Você é um adolescente".

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
    
    # Entrada da idade
    print_header("ENTRADA")
    
    try:
        idade = int(input("Digite a idade: "))
        if idade < 0:
            raise ValueError("Idade não pode ser um número negativo")
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
   
    print_header("SAÍDA")
    
    # Se for maior ou igual a 18
    if idade >= 18:
        # Saída maior de idade
        print("Maior de idade")
    
    # Se for maior ou igual a 12
    elif idade >= 12:
        # Saída adolescente
        print("Você é um adolescente")
        
    # Se for menor que 12
    else:
        # Saída criança
        print("Você é uma criança")

if __name__ == '__main__':
    main()

    
"""
========================================================================
TEST CASE
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
5
------------------------------------------------------------------------
[Saída esperada]
Você é uma criança

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
12
------------------------------------------------------------------------
[Saída esperada]
Você é um adolescente

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
17
------------------------------------------------------------------------
[Saída esperada]
Você é um adolescente

========================================================================

TC-04:
------------------------------------------------------------------------
[Entrada]
18
------------------------------------------------------------------------
[Saída esperada]
Maior de idade

========================================================================

TC-05:
------------------------------------------------------------------------
[Entrada]
-2
------------------------------------------------------------------------
[Saída esperada] 
Erro: Entrada inválida. -- Idade não pode ser um número negativo

========================================================================

TC-06:
------------------------------------------------------------------------
[Entrada] 
dez
------------------------------------------------------------------------
[Saída esperada]
Erro: Entrada inválida. -- (informações sobre o erro)

========================================================================
"""