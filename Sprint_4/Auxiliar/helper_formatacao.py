"""

Funções auxiliares para formatar a saída no terminal.

"""

def print_header(titulo, divisor="=", quantidade=30):
    """Imprime um cabeçalho para formatação das saídas no terminal.

    Args:
        titulo (str): Título do cabeçalho
        divisor (str, optional): Caractere para a linha divisora. Defaults to "=".
        quantidade (int, optional): Número de caracteres na linha divisora. Defaults to 30.
    """
    print(divisor*quantidade)
    print(titulo)
    print(divisor*quantidade)


def _print_chave_valor(chave, valor, recuo, incremento, char_recuo):
    """Função auxiliar para print_json().
    
    Apresenta, com formatação, um par de chave-valor de um objeto JSON.

    Args:
        chave (str): O nome da chave.
        valor (vários): O valor associado à chave.
        recuo (int, optional): O nível inicial de recuo. Defaults to 0.
        incremento (int, optional): O incremento no número de caracteres a cada nível de recuo. Defaults to 4.
        char_recuo (str, optional): O caracter a ser utilizado nos recuos. Defaults to " ".
    """
    # Recuar linha pelo número de caracteres de recuo
    print(char_recuo*recuo, end="")
    
    # Apresentar chave, se houver
    if chave:
        print('"' + chave + '":  ', end="")
    
    # Se o valor for um dicionário
    if type(valor) is dict:

        # Imprime chave de abertura
        print("{", end="")
        
        # Se for um dicionário vazio
        if len(valor) == 0:
            # Fecha a chave e encerra este item
            print("}")
            return
        else:
            # Quebra de linha
            print()
        
        # Recursão para os items do dicionário, no próximo nível de recuo
        for c, v in valor.items():
            _print_chave_valor(c, v, recuo+incremento, incremento, char_recuo)
        
        
        # Recuar linha pelo número de caracteres de recuo
        print(char_recuo*recuo, end="")
        # Imprime chave de fechamento
        print("}")
        
    # Se o valor for uma lista
    elif type(valor) is list:
        # Imprime colchete de abertura
        print("[", end="")
        
        # Se for uma lista vazia
        if len(valor) == 0:
            # Fecha o colchete e encerra este item
            print("]")
            return
        else:
            # Quebra de linha
            print()
        
        # Recursão para os itens da lista, no próximo nível de recuo, sem chave
        for item in valor:
            _print_chave_valor(None, item, recuo+incremento, incremento, char_recuo)
        
        # Recuar linha pelo número de caracteres de recuo
        print(char_recuo*recuo, end="")
        # Imprime colchete de fechamento
        print("]")
    
    # Caso valor seja uma string
    elif type(valor) is str:
        # Imprime o valor entre aspas
        print('"' + valor + '"')
        
    # Caso não seja dicionário, lista ou string
    else:
        # Somente imprime o valor
        print(valor)
        
def print_json(objeto_json, recuo=2, incremento=4, char_recuo=" "):
    """Apresenta um objeto json (dict) formatado para facilitar a leitura

    Args:
        objeto_json (dict): O objeto json a ser apresentado
    """
    print("{")
    for chave, valor in objeto_json.items():
        _print_chave_valor(chave, valor, recuo, incremento, char_recuo)
    
    print("}")