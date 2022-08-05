"""Exercício 10 [10/28]

Enunciado:
    Crie um programa que recebe uma lista com três frutas e
    compare com uma lista com os valores ["maça", "banana", "pera"].

Autor:
    Pedro Favoreto Gaya - 29/07/2022
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
    
    # Lista que guardará as entradas
    lista = []
    
    # Limite de valores para receber da entrada
    limite = 3
    

    print_header("ENTRADA")

    print(f"Digite {limite} frutas:")
    # Enquanto a lista tiver menos que 3 frutas
    while len(lista) < limite:
        # Entrada das frutas
        try:
            # Prompt da entrada informando quantas entradas já foram inseridas
            prompt = f"[{len(lista)}/{limite}]>"
            
            entradas = input(prompt).split()
            
        except ValueError as err:
            print("Aviso: Entrada inválida. Linha descartada. Tente novamente. -- ", err)
            continue
        
        # Para cada nova entrada
        for item in entradas:
            # Se ainda couberem items na lista
            if len(lista) < limite:
                # Adiciona a entrada ao final da lista
                lista.append(item)
            
            # Se não couberem mais itens na lista
            else:
                print("Limite de frutas atingido. Descartando entrada:", item)
    
    # Lista para comparação
    comparacao = ["maça", "banana", "pera"]
    
    
    print_header("SAÍDA")
    
    print("Comparando as seguintes listas:")
    # Apresenta a lista de entrada
    print("- ", end="")
    for fruta in lista:
        print(fruta, end=" ")
    print()
    
    # Apresenta a lista de comparação
    print("- ", end="")
    for fruta in comparacao:
        print(fruta, end=" ")
    print()
        
    # Verifica se as listas são iguais
    if lista == comparacao:
        print("As listas são iguais.")
    else:
        print("As listas são diferentes.")
        
    # Set com as frutas em comum
    comum = {fruta for fruta in lista if fruta in comparacao}
    
    # Se não houverem frutas em comum
    if len(comum) == 0:
        # Saída
        print("As listas não têm frutas em comum.")
    
    # Caso contrário
    else:
        # Apresenta as frutas em comum
        print("Frutas em comum: ", end="")
        for fruta in comum:
            print(fruta, end=" ")
            
        print()
            
    print("="*30)

if __name__ == '__main__':
    main()
   
    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
uva abacaxi manga
------------------------------------------------------------------------
[Saída esperada]
Comparando as seguintes listas:
- uva abacaxi manga
- maça banana pera
As listas são diferentes.
As listas não têm frutas em comum.

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
maça banana pera
------------------------------------------------------------------------
[Saída esperada]
COmparando as seguintes listas:
- maça banana pera
- maça banana pera
As listas são iguais.
Frutas em comum: maça banana pera

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
maça uva maça
------------------------------------------------------------------------
[Saída esperada]
Comparando as seguintes listas:
- maça uva maça
- maça banana pera
As listas são diferentes.
Frutas em comum: maça

========================================================================
"""