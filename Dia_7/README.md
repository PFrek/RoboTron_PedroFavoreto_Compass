# Exercícios Dia 7

![progress-bar](https://progress-bar.dev/10/?scale=16&title=solucionados&width=200&suffix=/16)

Esta pasta contém as soluções dos exercícios de Python disponibilizados no Dia 7 da trilha.

**Tema:** Manipulação de Arquivos Python

## Links

[**Link JSON 1**](https://pastebin.com/amF0XHEa)  
[**Link JSON 2**](https://pastebin.com/GxdV3pRP)  
[**Link CSV**](https://pastebin.com/LndbVMRT)  

-----

## Enunciados dos exercícios

> ### Exercício 01 -- [13/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_01.py)
> 
> Baixe o arquivo do link **JSON 1**, abra ele no vsCode com Python nomeando-o como partida, guarde em uma variável e printe o JSON inteiro no terminal.

-----

> ### Exercício 02 -- [14/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_02.py)
> 
> Pegue o arquivo **JSON 1** e printe apenas o nome do time vencedor no terminal.

-----

> ### Exercício 03 -- [15/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_03.py)
> 
> Do **JSON 1** Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

-----

> ### Exercício 04 -- [16/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_04.py)
> 
> No **JSON 1** printe todas as chaves e valores do time visitante.

-----

> ### Exercício 05 -- [17/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_05.py)
> 
> Guarde o arquivo **JSON 2** nomeando-o como **campeonato** em uma variável e printe todos os seus dados.

-----

> ### Exercício 06 -- [18/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_06.py)
> 
> Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o **JSON 2**.
>
> Obs.: Implementação exige Python versão 3.7 ou acima, pois espera que dicionários sejam ordenados por ordem de inserção.

-----

> ### Exercício 07 -- [19/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_07.py)
> 
> Percorra o **JSON 2**, utilizando o loop FOR e printe suas chaves principais.

-----

> ### Exercício 08 -- [20/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_08.py)
> 
> Abra o arquivo **CSV** com Pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal.

-----

> ### Exercício 09 -- [21/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_09.py)
> 
> Usando Pandas, leia apenas os dados da coluna Age do **CSV**.

-----

> ### Exercício 10 -- [22/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
> [Solução](https://github.com/PFrek/RoboTron_Pedro_Favoreto_Compass/blob/develop/Dia_7/exercicio_10.py)
> 
> Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

-----

> ### Exercício 11 -- [23/28] ![Fácil](https://img.shields.io/badge/-F%C3%A1cil-brightgreen)
> 
> Printe o nome do Ator que ganhou o Oscar em 1993.

-----

> ### Exercício 12 -- [24/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
> 
> Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

-----

> ### Exercício 13 -- [25/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
>
> Crie mais uma coluna em tempo de execução juntando os dados movie e year.

-----

> ### Exercício 14 -- [26/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
> 
> Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

-----

> ### Exercício 15 -- [27/28] ![Médio](https://img.shields.io/badge/-M%C3%A9dio-yellow)
>
> Mostre todos os filmes menos o "The Revenant".

-----

## Exercício final de leitura de dados CSV e JSON -- [28/28] ![Difícil](https://img.shields.io/badge/-Dif%C3%ADcil-red)

**Em Python crie uma aplicação que mostre elementos específicos em uma tabela periódica:**

A aplicação deve ter no mínimo 15 elementos da tabela periódica, não precisa ser todos pois são muitos, escolha os que você quiser.

Crie um CSV com um header contendo:

> Simbolo, Nome, NumeroAtomico, Linha, Coluna, EstadoFisico.

E adicione abaixo nas colunas os respectivos dados retirados do seguinte site:

<https://ptable.com/#Propriedades>

Exemplo:
> Simbolo, Nome, NumeroAtomico, Linha, Coluna, EstadoFisico  
> Cr, Cromio, 24, 4, 6, Solido

**Faça isso com no mínimo 15 elementos, aí já terá o CSV pronto para manipular.**

A) Crie uma "aplicação" em loop que tenha uma opção para listar todos os elementos da tabela, porém monstrando apenas uma propriedade do elemento. Ex: listar todos os nomes dos elementos na tabela.

B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

C) Listar todos os dados de todos os elementos inseridos.