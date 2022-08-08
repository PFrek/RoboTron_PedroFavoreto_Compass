"""
Dada uma sequência como:
78	39	29	12	92	11	18	2	12	1	68	44	74	15	12	17	42	84	65	67

1. Substituir tabs por espaço único
2. Extrair os números pares
3. Formato da saída:

Sequência: 78 39 29 12 92 11 18 2 12 1 68 44 74 15 12 17 42 84 65 67
Pares: 78 12 92 18 2 12 68 44 74 12 42 84
Média: 44.8333333333 

"""


# Função main
def main():
    # Entrada da sequência
    sequencia = list(map(int, input().split('\t')))
    
    # String da sequência
    string_seq = "Sequência: " + ' '.join(map(str, sequencia))
    
    # Pares
    pares = []
    for n in sequencia:
        if n % 2 == 0:
            pares.append(n)            
    
    # String dos pares
    string_pares = "Pares: " + ' '.join(map(str, pares))
    
    string_media = "Média: "
    # Cálculo da média
    if len(pares) > 0:
        media = sum(pares) / len(pares)
        string_media += str(media)
    else:
        string_media += "indefinida"
        
    print('\n'.join([string_seq, string_pares, string_media]))

if __name__ == '__main__':
    main()