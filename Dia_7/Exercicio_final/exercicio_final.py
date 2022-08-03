"""Exercício Final [28/28]

Enunciado:
    Requisito: elementos.csv --> Arquivo csv contendo informações de
    15 elementos da tabela periódica.

    A) Crie uma "aplicação" em loop que tenha uma opção de listar todos
    os elementos da tabela, porém mostrando apenas uma propriedade do
    elemento. Ex: listar todos os nomes dos elementos na tabela.
    
    B) Listar todos os dados de determinado elemento, buscando através
    do seu símbolo.
    
    C) Listar todos os dados de todos os elementos inseridos.

Autor:
    Pedro Favoreto Gaya - [Data]
"""

import pandas as pd

# Classe da aplicação
class TabelaPeriodica:
    # DataFrame contendo as informações dos elementos
    _elementos_df = pd.DataFrame()
    
    # Sinalizador para encerrar o loop
    _parar_loop = False
    
    # Dicionário com comandos disponíveis e as suas funções
    _comandos_dict = { }
    
    def __init__(self, arquivo_csv=None):
        # Se o argumento arquivo_csv estiver presente
        if arquivo_csv:
            # Tenta carregar o arquivo csv
            self.carregar_csv(arquivo_csv)
            
        # Exibe o header da aplicação
        self._print_header()
        
        # Constrói o dicionário de comandos válidos a partir dos elementos
        self._construir_comandos()
    
    def _print_separador(self, caracter="=", quantidade=80):
        print(caracter*quantidade)
                
    def _print_header(self):
        self._print_separador()
        print("TABELA PERIÓDICA")
        self._print_separador()
        print("Para uma lista de comandos disponíveis, digite 'comandos'.")
        self._print_separador("-")
    
    def carregar_csv(self, arquivo_csv):
        # Leitura do arquivo csv
        try:
            self._elementos_df = pd.read_csv(arquivo_csv, encoding="UTF-8", sep=",")
        except FileNotFoundError as err:
            self._print_separador()
            print(f"Aviso: arquivo csv {arquivo_csv} não encontrado. -- {err}")
            self._print_separador()
        else:
            self._print_separador()
            print(f"Arquivo CSV {arquivo_csv} carregado com sucesso.")
            self._print_separador()
        
    
    def _construir_comandos(self):
        # Estrutura da tupla de comando:
        # [0]: Função correspondente ao comando
        # [1]: Argumento a ser passado à função. None se não houver argumentos.
        
        # Comando para exibir os comandos válidos
        self._comandos_dict["comandos"] = (self._exibir_comandos, None)
        
        # Comando para encerrar o loop
        self._comandos_dict["parar"] = (self._parar, None)
        
        # Comando para listar todos os elementos e todas as propriedades
        self._comandos_dict["todos"] = (self._exibir_todos_elementos, None)
        
        # Se o DataFrame de elementos não estiver vazio
        if not self._elementos_df.empty:
            # Lista com os títulos de coluna
            titulos = self._elementos_df.columns
            
            # Para cada título de coluna
            for titulo in titulos:
                # Adiciona a função de busca por propriedade (título)
                # e o argumento a ser passado
                self._comandos_dict[str.lower(titulo)] = (self._exibir_propriedade, titulo)
            
            
            # Lista com os símbolos dos elementos
            simbolos = list(self._elementos_df["Simbolo"])
            
            # Para cada símbolo de elemento
            for simbolo in simbolos:
                # Adiciona a função de busca por elemento
                self._comandos_dict[simbolo] = (self._exibir_elemento, simbolo)
    
    
    def loop(self):
        self._parar_loop = False
        
        
        # Enquanto não for sinalizado para parar o loop
        while not self._parar_loop:
            # Ler a entrada
            funcao, argumento = self._ler_entrada()
            
            # Se uma função foi encontrada
            if funcao:
                
                # Se um argumento foi recebido
                if argumento:
                    # Executar a função com o argumento
                    funcao(argumento)
                else:
                    # Executar a função sem argumentos    
                    funcao()
    
    def _ler_entrada(self):
        # Exibe o prompt para a entrada
        print("TabelaPeriodica > ", end="")
        
        # Recebe a entrada do usuário
        entrada = input()
        
        # Se a entrada for uma chave válida do dicionário de comandos
        if entrada in self._comandos_dict:
            # Retorna a tupla contendo a funcao e o argumento
            # correspondente ao comando
            return self._comandos_dict[entrada]
        else:
            self._print_separador("-")
            print("Aviso: comando inválido.")
            print("Para uma lista de comandos disponíveis, digite 'comandos'.")
            self._print_separador("-")
            
            # Retorno para caso de erro
            return (None, None)
    
    def _parar(self):
        self._parar_loop = True
        self._print_separador()
        print("Encerrando a aplicação.")
        self._print_separador()
    
    def _exibir_comandos(self):
        # Lista de propriedades aceitas
        lista_propriedades = []
        # Lista de simbolos de elementos aceitos
        lista_simbolos = []
        
        # Para cada comando válido
        for chave, comando in self._comandos_dict.items():
            # Se o comando for para exibir uma propriedade
            if comando[0] == self._exibir_propriedade:
                # Adiciona às propriedades válidas
                lista_propriedades.append(chave)
                
            # Se o comando for para exibir um elemento
            elif comando[0] == self._exibir_elemento:
                # Adiciona aos simbolos válidos
                lista_simbolos.append(chave)
                
        self._print_separador()
        print("Lista de comandos disponíveis:")
        print("- comandos : Exibe todos os comandos disponíveis.")
        print("- parar : Encerra o loop da aplicação.")
        print("- todos : Exibe todas as propriedades de todos os elementos.")
        print("- [Nome da propriedade]: Exibe uma propriedade de todos os elementos.")
        print("\t. Propriedades disponíveis:")
        print("\t-", ", ".join(lista_propriedades))
        print("- [Símbolo do elemento] : Exibe todas as propriedades de um único elemento.")
        print("\t. Elementos disponíveis:")
        print("\t-", ", ".join(lista_simbolos))
        self._print_separador()    
        
    def _exibir_todos_elementos(self):
        # Exibe todo o DataFrame dos elementos
        self._print_separador("-")
        print(self._elementos_df)
        self._print_separador("-")
    
    def _exibir_propriedade(self, propriedade):
        
        # Lista de colunas a serem buscadas
        colunas = []
            
        # Adiciona a propriedade às colunas buscadas
        colunas.append(propriedade)
        
        resultado_df = self._elementos_df[colunas]
        
        # Se a propriedade não for o próprio símbolo
        if propriedade != "Simbolo":
            # Usa os símbolos como índices para facilitar a identificação
            resultado_df.set_index(self._elementos_df["Simbolo"], inplace=True)
            resultado_df.index.name = None
        
    

        self._print_separador("-")
        print(resultado_df)
        self._print_separador("-")
    
    def _exibir_elemento(self, simbolo):
       # DataFrame contendo as informações do elemento
       elemento = self._elementos_df.loc[
           self._elementos_df["Simbolo"] == simbolo
       ]
       
       self._print_separador("-")
       print(elemento)
       self._print_separador("-")
    

# Função main
def main():
    tabela = TabelaPeriodica("elementos.csv")

    tabela.loop()
    

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
(vazia)

========================================================================
""" 
