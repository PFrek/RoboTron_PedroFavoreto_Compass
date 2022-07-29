"""Exercício 5 [05/28]

Enunciado:
    Construa um programa que recebe 20 valores para X e no final apresenta a
    média aritmética dos valores pares digitados.

Autor:
    Pedro Favoreto Gaya - 28/07/2022
    
Referências:
    Comportamento para média de conjunto vazio:
    https://math.stackexchange.com/questions/909395/what-is-the-arithmetic-mean-of-no-numbers
"""

# Função main
def main():
    # Lista que guardará os números entrados
    numeros = []
    
    # Variável que guardará a soma dos valores pares
    soma = 0
    
    # Contador de números pares da entrada
    n_pares = 0
    
    # Limite de valores para receber da entrada
    limite = 20
    
    print("="*30)
    print("ENTRADA")
    print("="*30)
    
    print(f"Digite {limite} números: ")
    # Enquanto a lista tiver menos que 20 itens
    while len(numeros) < limite:
        # Recebe uma entrada /ou/ várias entradas separadas por espaço
        try:
            prompt = f"[{str(len(numeros)).zfill(2)}/{limite}]>"
            
            entradas = list(map(int, input(prompt).split()))
            
        except ValueError as err:
            print("Aviso: Entrada inválida. Linha descartada. Tente novamente. -- ", err)
            continue
        
        # Para cada nova entrada
        for item in entradas:
            # Se ainda couberem itens na lista
            if len(numeros) < limite:
                # Adiciona a entrada à lista
                numeros.append(item)
            
                # Se for um valor par
                if item % 2 == 0:
                    # Adiciona o valor à soma
                    soma += item
                    
                    # Incrementa o contador de números pares
                    n_pares += 1
            
            # Se não couberem mais itens na lista
            else:
                print("Limite de valores atingido. Descartando entrada:", item)
    
    print("="*30)
    print("SAÍDA")
    print("="*30)
    
    # Se a entrada não contém nenhum valor par
    if n_pares == 0:
        
        # Saída
        print("Nenhum valor par encontrado na entrada: média indefinida")

    # Caso contrário
    else:    
        # Calcula a média
        media = soma / n_pares

        # Saída
        print("Média dos valores pares:", media)
        
    

if __name__ == '__main__':
    main()
    
"""
------------------------------------------------------------------------
TEST CASES
------------------------------------------------------------------------

Sequências geradas em: https://www.random.org/integers/
Parâmetros:
    - 120 números gerados
    - Números entre 1 e 100

Conferência da média feita no site:
https://miniwebtool.com/br/mean-calculator/

------------------------------------------------------------------------
TC-00:
Sequência: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39
Pares: (conjunto vazio)
Média: indefinida
------------------------------------------------------------------------
TC-01:
Sequência: 78 39 29 12 92 11 18 2 12 1 68 44 74 15 12 17 42 84 65 67
Pares: 78 12 92 18 2 12 68 44 74 12 42 84
Média: 44.8333333333
------------------------------------------------------------------------
TC-02:
Sequência: 75 24 70 4 73 60 60 41 81 12 96 78 45 58 13 5 80 26 35 36
Pares: 24 70 4 60 60 12 96 78 58 80 26 36
Média: 50.3333333333
------------------------------------------------------------------------
TC-03:
Sequência: 41 72 25 21 10 65 23 68 70 29 2 53 70 15 82 22 47 75 54 75
Pares: 72 10 68 70 2 70 82 22 54
Média: 50
------------------------------------------------------------------------
TC-04:
Sequência: 5 55 8 89 26 3 56 57 60 50 72 10 60 2 74 31 77 2 41 40
Pares: 8 26 56 60 50 72 10 60 2 74 2 40
Média: 38.3333333333
------------------------------------------------------------------------
TC-05:
Sequência: 43 76 73 19 74 53 13 26 69 16 12 25 95 54 28 45 97 89 58 3
Pares: 76 74 26 16 12 54 28 58
Média: 43
------------------------------------------------------------------------
TC-06:
Sequência: 75 5 35 17 30 72 97 36 60 100 5 78 81 46 36 55 81 58 17 86
Pares: 30 72 36 60 100 78 46 36 58 86
Média: 60.2
------------------------------------------------------------------------
"""