"""Exercício 1 [13/28]

Enunciado:
    Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o
    como partida, guarde em uma variável e printe o JSON inteiro no terminal.

Autor:
    Pedro Favoreto Gaya - 01/08/2022
    
Referências:
    Correção do caminho relativo do arquivo:
    https://stackoverflow.com/questions/918154/relative-paths-in-python
"""

import json
import os

from helper_formatacao import print_header

def abrir_json(nome_arquivo):
    """Abre um arquivo JSON e retorna o seu conteúdo.

    Args:
        nome_arquivo (String): caminho relativo para o arquivo json.

    Returns:
        dict: Dicionário com o conteúdo do arquivo aberto.
    """
    # Montagem do caminho absoluto para o arquivo.
    # Permite executar o script a partir de outras pastas, sem que haja erro.
    diretorio = os.path.dirname(__file__)
    nome_arquivo = os.path.join(diretorio, nome_arquivo)
    
    with open(nome_arquivo, encoding="UTF-8") as arquivo:
        conteudo_json = json.load(arquivo)
        return conteudo_json

# Função main
def main():
    # Leitura do arquivo json
    partida_json = abrir_json("dados/partida.json")
    
    # Saída do json completo
    print_header("SAÍDA")
    
    print(partida_json)


if __name__ == '__main__':
    main()
    
    
"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
(vazia)
------------------------------------------------------------------------
[Saída esperada]
(Conteúdo do arquivo json "partida.json")

========================================================================
""" 
