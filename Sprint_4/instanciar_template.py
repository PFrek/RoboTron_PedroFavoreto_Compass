"""

Cria um script para um novo exercício a partir do template

Como usar:
    py instanciar_template.py [Dia] [numero do exercicio]

Referência:
    Command Line Args in Python:
    https://realpython.com/python-command-line-arguments/
    
"""
import sys
from os.path import exists
import datetime


# Função main
def main():
    # Se o programa tiver o número incorreto de argumentos
    if len(sys.argv) != 3:
        # Saída de erro
        print("Número incorreto de argumentos - Como usar: py instanciar_template.py [Dia] [numero do exercicio]")
        return
        
    dia = sys.argv[1]
    n_exercicio = sys.argv[2]
    
    if int(dia) not in [5, 7]:
        print("Dia inválido")
        return
    
    # Caminho do arquivo a ser gerado
    novo_script = f"Dia_{dia}/exercicio_{n_exercicio.zfill(2)}.py"
    
    # Se o arquivo já existir
    if exists(novo_script):
        # Saída de erro
        print("Arquivo " + novo_script + " já existe.")
        return
        
    
    # Linhas do template
    linhas = []
    # Abre o arquivo de template
    with open('template.py', 'r') as f:
        # Extrai as linhas do template
        linhas = f.readlines()
        
    # Substitui X da primeira linha pelo número do exercício
    linhas[0] = linhas[0].replace("X", n_exercicio)
    
    # Substitui YY da primeira linha pelo número total do exercício
    if int(dia) == 5:
        linhas[0] = linhas[0].replace("YY", n_exercicio.zfill(2))
    elif int(dia) == 7:
        linhas[0] = linhas[0].replace("YY", str(int(n_exercicio)+12))
    
    data = datetime.datetime.now()
    # Substitui [Data] da linha 7 pela data de hoje
    linhas[6] = linhas[6].replace("[Data]", 
                                  '/'.join([
                                        str(data.day).zfill(2),
                                        str(data.month).zfill(2),
                                        str(data.year)
                                    ]))
    
    # Abre o novo arquivo de script
    with open(novo_script, 'w') as f:
        # Insere as linhas alteradas do template
        f.writelines(linhas)

if __name__ == '__main__':
    main()
