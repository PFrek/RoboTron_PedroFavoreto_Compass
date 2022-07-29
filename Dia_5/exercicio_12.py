"""Exercício 12 [12/28]

Enunciado:
    Leia um valor inteiro correspondente à idade de uma pessoa em dias
    e informe-a em anos, meses e dias.
    Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias
    e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação
    que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas
    um exercício com objetivo de testar raciocínio matemático simples.

Autor:
    Pedro Favoreto Gaya - 29/07/2022
"""


# Função main
def main():
    
    print("="*30)
    print("ENTRADA")
    print("="*30)
    
    # Entrada da idade em dias
    try:
        prompt = "Digite a idade em dias: "
        
        idade_dias = int(input(prompt))
        
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    # Quantidade de anos
    idade_anos = idade_dias // 365
    
    # Restante dos dias além dos anos
    idade_dias %= 365
    
    # Quantidade de meses
    idade_meses = idade_dias // 30
    
    # Restante dos dias além dos meses = quantidade de dias
    idade_dias %= 30
    
    print("="*30)
    print("SAÍDA")
    print("="*30)
    
    # Saída
    print(f"{idade_anos} ano(s)")
    print(f"{idade_meses} mes(es)")
    print(f"{idade_dias} dia(s)")

if __name__ == '__main__':
    main()
   
    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
400
------------------------------------------------------------------------
[Saída esperada]
1 ano(s)
1 mes(es)
5 dia(s)

========================================================================

TC-02:
------------------------------------------------------------------------
[Entrada]
800
------------------------------------------------------------------------
[Saída esperada]
2 ano(s)
2 mes(es)
10 dia(s)

========================================================================

TC-03:
------------------------------------------------------------------------
[Entrada]
30
------------------------------------------------------------------------
[Saída esperada]
0 ano(s)
1 mes(es)
0 dia(s)

========================================================================
"""