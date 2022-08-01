"""Exercício 11 [11/28]

Enunciado:
    Leia a hora inicial e a hora final de um jogo. A seguir calcule a
    duração do jogo, sabendo que o mesmo pode começar em um dia e terminar
    em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
    Entrada: A entrada contém dois valores inteiros representando a hora
    de início e a hora de fim do jogo.
    Saída: Apresente a duração do jogo conforme exemplo abaixo.

Autor:
    Pedro Favoreto Gaya - 29/07/2022
"""

from helper_formatacao import print_header

# Função main
def main():    
    
    # Entrada das horas inicial e final do jogo
    print_header("ENTRADA")
    
    try:
        prompt = "Digite a hora inicial e a hora final do jogo: "
        
        hora_inicial, hora_final = map(int, input(prompt).split(" "))
        
        # Verifica horas inválidas
        if hora_inicial not in range(0, 24) or hora_final not in range(0, 24):
            raise ValueError("Hora deve ser um inteiro entre [0 e 23]")
        
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    # Variável que guardará a duração do jogo
    duracao = 0
    
    # Caso base: se as horas forem iguais, duracao = 24 horas
    if hora_inicial == hora_final:
        duracao = 24
    
    # Caso contrário
    else:
        # Se a hora final for menor que a hora inicial
        if hora_final < hora_inicial:
            # Hora final está no dia seguinte, adiciona 24 horas ao seu valor
            hora_final += 24
            
        # Duracao = hora final - hora inicial
        duracao = hora_final - hora_inicial
    
    
    # Saída
    print_header("SAÍDA")
    
    print(f"O JOGO DUROU {duracao} HORA(S)")


if __name__ == '__main__':
    main()
    
    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
16 2
------------------------------------------------------------------------
[Saída esperada]
O JOGO DUROU 10 HORA(S)

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
0 0
------------------------------------------------------------------------
[Saída esperada]
O JOGO DUROU 24 HORA(S)

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
2 16
------------------------------------------------------------------------
[Saída esperada]
O JOGO DUROU 14 HORA(S)

========================================================================
""" 