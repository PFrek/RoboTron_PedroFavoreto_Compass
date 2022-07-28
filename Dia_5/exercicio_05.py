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
    
    
    print("Digite 20 números: ")
    # Enquanto a lista tiver menos que 20 itens
    while len(numeros) < 20:
        # Recebe uma entrada /ou/ várias entradas separadas por espaço
        try:
            entradas = list(map(int, input().split()))
        except ValueError as err:
            print("Aviso: Entrada inválida. Linha descartada. Tente novamente. -- ", err)
            continue
        
        # Para cada nova entrada
        for entrada in entradas:
            # Adiciona a entrada à lista
            numeros.append(entrada)
            
            # Se for um valor par
            if entrada % 2 == 0:
                # Adiciona o valor à soma
                soma += entrada
                
                # Incrementa o contador de números pares
                n_pares += 1
    
    # Se a entrada não contém nenhum valor par
    if n_pares == 0:
        
        # Saída
        print("Nenhum valor par encontrado na entrada: média indefinida")

    # Caso contrário
    else:    
        # Calcula a média
        media = soma / n_pares

        # Saída
        print("Média:", media)
        
    

if __name__ == '__main__':
    main()
    
"""
------------------------------------------------------------------------
TEST CASES
------------------------------------------------------------------------

Sequências geradas em: https://www.random.org/integers/
Parâmetros:
    - 200 números gerados
    - Números entre 1 e 100

Conferência da média feita no site:
https://miniwebtool.com/br/mean-calculator/

------------------------------------------------------------------------
TC-00:
Sequência: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41
Pares: (conjunto vazio)
Média: indefinida
------------------------------------------------------------------------
TC-01:
Sequência: 78 39 29 12 92 11 18 2 12 1 68 44 74 15 12 17 42 84 65 67
Pares: 78 12 92 18 2 12 68 44 74 12 42 84
Média: 44.833333333333336
------------------------------------------------------------------------
TC-02:
Sequência: 75 24 70 4 73 60 60 41 81 12 96 78 45 58 13 5 80 26 35 36
Pares: 24 70 4 60 60 12 96 78 58 80 26 36
Média: 50.333333333333336
------------------------------------------------------------------------
TC-03:
Sequência: 41 72 25 21 10 65 23 68 70 29 2 53 70 15 82 22 47 75 54 75
Pares: 72 10 68 70 2 70 82 22 54
Média: 50.0
------------------------------------------------------------------------
TC-04:
Sequência: 5 55 8 89 26 3 56 57 60 50 72 10 60 2 74 31 77 2 41 40
Pares: 8 26 56 60 50 72 10 60 2 74 2 40
Média: 38.333333333333336
------------------------------------------------------------------------
TC-05:
Sequência: 43 76 73 19 74 53 13 26 69 16 12 25 95 54 28 45 97 89 58 3
Pares: 76 74 26 16 12 54 28 58
Média: 43.0
------------------------------------------------------------------------
TC-06:
Sequência: 75 5 35 17 30 72 97 36 60 100 5 78 81 46 36 55 81 58 17 86
Pares: 30 72 36 60 100 78 46 36 58 86
Média: 60.2
------------------------------------------------------------------------
TC-07:
Sequência: 49 91 58 100 50 88 89 16 82 10 52 22 78 20 100 66 88 5 24 13
Pares: 58 100 50 88 16 82 10 52 22 78 20 100 66 88 24
Média: 56.93333333333333
------------------------------------------------------------------------
TC-08:
Sequência: 5 66 48 23 51 56 16 45 16 98 11 4 86 62 79 42 26 28 5 4
Pares: 66 48 56 16 16 98 4 86 62 42 26 28 4
Média: 42.46153846153846
------------------------------------------------------------------------
TC-09:
Sequência: 27 69 13 30 12 68 55 34 50 44 68 25 1 51 95 65 66 54 26 60
Pares: 30 12 68 34 50 44 68 66 54 26 60
Média: 46.54545454545455
------------------------------------------------------------------------
TC-10:
Sequência: 32 38 4 37 41 89 45 59 95 63 33 43 40 24 20 47 10 77 3 67
Pares: 32 38 4 40 24 20 10
Média: 24.0
------------------------------------------------------------------------
"""