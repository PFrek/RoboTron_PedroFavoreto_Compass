"""Exercício 9 [09/28]

Enunciado:
    Crie um programa que recebe 15 valores e armazena em uma lista,
    e no final da execução mostre os valores da lista do último para
    o primeiro.

Autor:
    Pedro Favoreto Gaya - 29/07/2022
    
Referência:
    Documentação sobre listas
    https://docs.python.org/3/tutorial/datastructures.html
"""


# Função main
def main():
    # Lista que guardará os números
    lista = []
    
    # Limite de valores para receber da entrada
    limite = 15
    
    print("="*30)
    print("ENTRADA")
    print("="*30)
    print(f"Digite {limite} valores:")
    # Enquanto a lista não tiver 15 valores
    while len(lista) < limite:
        # Entrada dos valores
        try:
            prompt = f"[{str(len(lista)).zfill(2)}/{limite}]>"
            
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
                print("Limite de valores atingido. Descartando entrada:", item)
    
    print("="*30)
    print("SAÍDA")
    print("="*30)
    # Apresenta a lista do último para o primeiro valor
    for valor in reversed(lista):
        print(valor, end=" ")
        
        
    print()


if __name__ == '__main__':
    main()
    

"""
------------------------------------------------------------------------
TEST CASES
------------------------------------------------------------------------

Sequências geradas em: https://www.random.org/integers/
Parâmetros:
    - 15 números gerados
    - Números entre 1 e 100
------------------------------------------------------------------------
TC-01: (Inteiros)
Entrada: 28 25 85 58 98 42 55 80 13 86 58 74 74 61 27
Saída esperada: 27 61 74 74 58 86 13 80 55 42 98 58 85 25 28
------------------------------------------------------------------------
TC-02: (Decimais)
Entrada: 0.72 0.22 0.75 0.64 0.27 0.58 0.42 0.53 0.62 0.16 0.27 0.56 0.17 0.92 0.06
Saída esperada: 0.06 0.92 0.17 0.56 0.27 0.16 0.62 0.53 0.42 0.58 0.27 0.64 0.75 0.22 0.72
------------------------------------------------------------------------
TC-03: (Strings)
Entrada: RVnsO nMKGV QnTVt miqwR nNRUU MBXGt NAviC uJGnO rBHJL sjwRF kUzTW ugpME QFYSa nwvQL djJOk
Saída esperada: djJOk nwvQL QFYSa ugpME kUzTW sjwRF rBHJL uJGnO NAviC MBXGt nNRUU miqwR QnTVt nMKGV RVnsO 
------------------------------------------------------------------------
"""