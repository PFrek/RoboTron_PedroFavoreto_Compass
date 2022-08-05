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
    Pedro Favoreto Gaya - 03/08/2022
"""
import os

import pandas as pd

# Classe da aplicação
class TabelaPeriodica:   
    """
    .---------------------------------------.
    | Métodos de Inicialização              |
    |---------------------------------------|
    |                                       |
    | __init__(self, arquivo_csv=None)      |
    |                                       |
    | carregar_csv(self, arquivo_csv)       |
    |                                       |
    | _construir_comandos(self)             |
    *---------------------------------------*
    """
    
    def __init__(self, arquivo_csv=None):
        """Construtor da aplicação.

        Args:
            arquivo_csv (str, optional): Caminho para um arquivo csv a ser carregado. Defaults to None.
        """
        # Variáveis de instância
    
        # DataFrame contendo as informações dos elementos
        self._elementos_df = pd.DataFrame()
        
        # Sinalizador para encerrar o loop
        self._parar_loop = False
        
        # Dicionário com comandos disponíveis e as suas funções
        self._comandos_dict = { }
        

        
        # Tenta carregar o arquivo csv
        self.carregar_csv(arquivo_csv)
            
        # Exibe o header da aplicação
        self._exibir_header()
        
        # Constrói o dicionário de comandos válidos a partir dos elementos no csv carregado
        self._construir_comandos()
    
    
    def carregar_csv(self, arquivo_csv):
        """Carrega um DataFrame de um arquivo csv contendo as informações dos elementos.

        Args:
            arquivo_csv (str): Caminho para o arquivo csv.
        """
        # Leitura do arquivo csv
        try:
            # Montagem do caminho absoluto para o arquivo.
            # Permite executar o script a partir de outras pastas, sem que haja erro.
            diretorio = os.path.dirname(__file__)
            arquivo_csv = os.path.join(diretorio, arquivo_csv)
            
            self._elementos_df = pd.read_csv(arquivo_csv, encoding="UTF-8", sep=",")
        except FileNotFoundError as err:
            # Saída de erro, caso o arquivo não seja encontrado
            self._exibir_separador()
            print(f"Aviso: arquivo csv {arquivo_csv} não encontrado. -- {err}")
            self._exibir_separador()
        else:
            # Saída de sucesso
            self._exibir_separador()
            print(f"Arquivo CSV {arquivo_csv} carregado com sucesso.")
            self._exibir_separador()

            # Constrói o dicionário de comandos válidos da aplicação
            self._construir_comandos()        
        
    
    def _construir_comandos(self):
        """Insere os comandos e as funções válidas no dicionário de comandos.
        
        Cada comando consiste em uma palavra, que será comparada à entrada do
        usuário. Ele será inserido no dicionário como a chave.
        
        O valor associado a cada chave será uma tupla com a seguinte estrutura:
        [0]: Função correspondente ao comando.
        [1]: Argumento a ser passado à função. None se não houver argumentos.
        
        """
        # Reinicializar o dicionário de comandos
        self._comandos_dict = {}
        
        # Comando para exibir os comandos válidos
        self._comandos_dict["comandos"] = (self._exibir_comandos, None)
        
        # Comando para encerrar o loop
        self._comandos_dict["parar"] = (self._parar, None)
        
        # Comando para listar todos os elementos e todas as propriedades
        self._comandos_dict["todos"] = (self._exibir_todos_elementos, None)
        
        # Comando para carregar um novo arquivo csv
        self._comandos_dict["carregar"] = (self.carregar_csv, None)
        
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
    
    
    """
    ===========================================================================
    
    .---------------------------.
    | Métodos de Controle       |
    |---------------------------|
    |                           |
    | loop(self)                |
    |                           |
    | _ler_entrada(self)        |
    |                           |
    | _parar(self)              |
    |                           |
    *---------------------------*
    """
    
    def loop(self):
        """Inicia e mantém o loop principal da aplicação.
        """
        # Reinicialização da variável de controle
        self._parar_loop = False
        
        # Enquanto não for sinalizado para parar o loop
        while not self._parar_loop:
            # Ler a entrada
            funcao, argumento = self._ler_entrada()
            
            # Se uma função foi retornada
            if funcao:
                
                # Se um argumento foi recebido
                if argumento:
                    # Executar a função com o argumento
                    funcao(argumento)
                else:
                    # Executar a função sem argumentos    
                    funcao()
            
            # Caso contrário, aviso de erro
            else:
                self._exibir_separador("-")
                print("Aviso: comando inválido.")
                print("Para uma lista de comandos disponíveis, digite 'comandos'.")
                self._exibir_separador("-")
    
    
    def _ler_entrada(self):
        """Lê a entrada do usuário e busca por um comando equivalente.

        Returns:
            tuple: Tupla contendo a função e os argumentos a serem passados.
                    (None, None) em caso de erro.
        """
        # Exibe o prompt para a entrada
        print("TabelaPeriodica> ", end="")
        
        # Recebe a entrada do usuário
        entrada = input().split(" ")
        
        # Se a entrada estiver vazia
        if len(entrada) == 0:
            return (None, None)
        
        # A primeira palavra da entrada será o comando a ser procurado
        comando = entrada[0]
        
        # Se o comando for uma chave válida do dicionário de comandos
        if comando in self._comandos_dict:
            # Tupla encontrada no dicionário de comandos
            funcao, argumento = self._comandos_dict[comando]
            
            # Se o comando for "carregar"
            if comando == "carregar":
                # Se a entrada não tiver uma segunda palavra (caminho do csv)
                if len(entrada) < 2:
                    # Saída de erro
                    print("Comando 'carregar' necessita do caminho do arquivo csv a ser carregado.")
                    return (None, None)
                    
                # Altera o argumento para a segunda palavra (caminho do csv)
                argumento = entrada[1]
                
            return (funcao, argumento)
                
        else:            
            return (None, None)
    
    
    def _parar(self):
        """Encerra o loop principal da aplicação.
        """
        self._parar_loop = True
        
        self._exibir_separador()
        print("Encerrando a aplicação.")
        self._exibir_separador()
   
   
    """
    ===========================================================================
    
    .---------------------------------------------------.
    | Métodos de exibição                               |
    |---------------------------------------------------|
    |                                                   |
    | _exibir_separador(self, caracter, quantidade)     |
    |                                                   |
    | _exibir_header(self)                              |
    |                                                   |
    | _exibir_comandos(self)                            |
    |                                                   |
    | _exibir_todos_elementos(self)                     |
    |                                                   |
    | _exibir_propriedade(self, propriedade)            |
    |                                                   |
    | _exibir_elemento(self, simbolo)                   |
    |                                                   |
    *---------------------------------------------------*
    """
   
    def _exibir_separador(self, caracter="=", quantidade=80):
        """Exibe uma linha separadora no terminal.

        Args:
            caracter (str, optional): Caracter que comporá a linha. Defaults to "=".
            quantidade (int, optional): Tamanho da linha. Defaults to 80.
        """
        print(caracter*quantidade)
    
                
    def _exibir_header(self):
        """Exibe o cabeçalho da aplicação.
        """
        self._exibir_separador()
        print("TABELA PERIÓDICA")
        self._exibir_separador()
        print("Para uma lista de comandos disponíveis, digite 'comandos'.")
        self._exibir_separador("-")
    
    
    def _exibir_comandos(self):
        """Exibe a lista de comandos válidos da aplicação.
        """
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
        
        # Saída        
        self._exibir_separador()
        print("Lista de comandos disponíveis:")
        print("- comandos \t\t\tExibe todos os comandos disponíveis.")
        print("- parar \t\t\tEncerra o loop da aplicação.")
        print("- carregar [arquivo.csv] \tCarrega um novo arquivo csv contendo as informações dos elementos.")
        print("- todos \t\t\tExibe todas as propriedades de todos os elementos.")
        print("- [Nome da propriedade] \tExibe uma propriedade de todos os elementos.")
        print("\t\t\t\t. Propriedades disponíveis:")
        print("\t\t\t\t\t-", ", ".join(lista_propriedades))
        print("- [Símbolo do elemento] : \tExibe todas as propriedades de um único elemento.")
        print("\t\t\t\t. Elementos disponíveis:")
        print("\t\t\t\t\t-", ", ".join(lista_simbolos))
        self._exibir_separador()    
    
    
    # Parte C)
    def _exibir_todos_elementos(self):
        """Exibe todas as propriedades de todos os elementos.
        """
        # Exibe todo o DataFrame dos elementos
        self._exibir_separador("-")
        print(self._elementos_df)
        self._exibir_separador("-")
    
    
    # Parte A)
    def _exibir_propriedade(self, propriedade):
        """Exibe uma única propriedade de todos os elementos.

        Args:
            propriedade (str): Nome da propriedade que será exibida.
        """
            
        # Series contendo a coluna que se refere à propriedade
        resultado = self._elementos_df[propriedade]
        
        # Se a propriedade não for o próprio símbolo
        if propriedade != "Simbolo":
            # Usa os símbolos como índices para facilitar a identificação
            resultado.index = self._elementos_df["Simbolo"]
            resultado.index.name = None

        # Saída
        self._exibir_separador("-")
        print(resultado)
        self._exibir_separador("-")
    
    
    # Parte B)
    def _exibir_elemento(self, simbolo):
        """Exibe todas as propriedades de um único elemento.

        Args:
            simbolo (str): Símbolo do elemento que será exibido.
        """
        
        # DataFrame contendo as informações do elemento
        elemento_df = self._elementos_df.loc[
            self._elementos_df["Simbolo"] == simbolo
        ]
        
        # Saída
        self._exibir_separador("-")
        print(elemento_df)
        self._exibir_separador("-")
    

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

TC-01: (Listar comandos disponíveis)
------------------------------------------------------------------------
[Entrada]
comandos
------------------------------------------------------------------------
[Saída esperada]
(Lista com os comandos disponíveis da aplicação)

========================================================================
TC-02: (Listar Simbolos)
------------------------------------------------------------------------
[Entrada]
simbolo
------------------------------------------------------------------------
[Saída esperada]
(Series contendo todos os símbolos)

========================================================================

TC-03: (Listar números atômicos)
------------------------------------------------------------------------
[Entrada]
numeroatomico
------------------------------------------------------------------------
[Saída esperada]
(Series contendo todos os números atômicos, indexados pelos símbolos)

========================================================================

TC-04: (Buscar propriedade inexistente)
------------------------------------------------------------------------
[Entrada]
massaatomica
------------------------------------------------------------------------
[Saída esperada]
(separador)
Aviso: comando inválido.
Para uma lista de comandos disponíveis, digite 'comandos'.
(separador)

========================================================================
TC-05: (Listar todos os dados de um elemento)
------------------------------------------------------------------------
[Entrada]
Au
------------------------------------------------------------------------
[Saída esperada]
(DataFrame contendo as informações do elemento Au - Ouro)

========================================================================

TC-06: (Listar todos os dados de um elemento)
------------------------------------------------------------------------
[Entrada]
Rn
------------------------------------------------------------------------
[Saída esperada]
(DataFrame contendo as informações do elemento Rn - Radônio)

========================================================================

TC-07: (Buscar elemento não implementado)
------------------------------------------------------------------------
[Entrada]
Na
------------------------------------------------------------------------
[Saída esperada]
(separador)
Aviso: comando inválido.
Para uma lista de comandos disponíveis, digite 'comandos'.
(separador)

========================================================================

TC-08: (Listar todos os dados de todos os elementos)
------------------------------------------------------------------------
[Entrada]
todos
------------------------------------------------------------------------
[Saída esperada]
(DataFrame contendo as informações de todos os elementos)

========================================================================

TC-09: (Carregar novo arquivo csv)
------------------------------------------------------------------------
[Entrada]
carregar teste_carregar.csv
------------------------------------------------------------------------
[Saída esperada]
(separador)
Arquivo CSV teste_carregar.csv carregado com sucesso.
(separador)
------------------------------------------------------------------------
** Testar se os outros comandos apresentam apenas o conteúdo do novo
arquivo csv - (conteúdo: somente elemento Au - Ouro). **

========================================================================

TC-10: (Carregar arquivo csv inexistente)
------------------------------------------------------------------------
[Entrada]
carregar nao_existe.csv
------------------------------------------------------------------------
[Saída esperada]
(separador)
Aviso: arquivo csv nao_existe.csv não encontrado. -- (informações de erro)
(separador)
------------------------------------------------------------------------
** Testar se os outros comandos continuam funcionando para o arquivo
csv que já estava carregado. **

========================================================================
""" 
