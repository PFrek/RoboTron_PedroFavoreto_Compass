"""Exercício 4 [04/28]

Enunciado:
    Construa um programa que armazena uma idade em uma variável e compara,
    se a idade for maior que 18, apresenta "Maior de idade",
    se a idade for menor que 12, apresenta "Você é uma criança"
    e se for maior que 12 e menor que 18, apresenta "Você é um adolescente".

Autor:
    Pedro Favoreto Gaya - 27/07/2022
"""

# Função main
def main():
    
    print("="*30)
    print("ENTRADA")
    print("="*30)
    
    # Entrada da idade
    try:
        idade = int(input("Digite a idade: "))
        if idade < 0:
            raise ValueError("Idade não pode ser um número negativo")
    except ValueError as err:
        print("Erro: Entrada inválida. -- ", err)
        return
    
    print("="*30)
    print("SAÍDA")
    print("="*30)
    
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