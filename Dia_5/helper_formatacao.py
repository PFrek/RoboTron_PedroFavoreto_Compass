"""

Funções utilitárias para formatar a saída no terminal.

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