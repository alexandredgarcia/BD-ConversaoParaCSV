#PROGRAMA LIVRARIA....CONVERSÃO PARA ARQUIVO CSV
"""
Módulo: Conversor de Dados de Livraria para CSV
Descrição: Este programa cria um dicionário com informações sobre autores,
           livros e anos de publicação, converte esses dados em um DataFrame
           usando a biblioteca Pandas e os exporta para um arquivo CSV.
"""

# Importação da biblioteca Pandas para manipulação e análise de dados
import pandas as pd

# Definição das listas contendo os dados dos livros
autor = ['Sun Tzu','Fernando Pessoa','Thomaz Mann','João Guimarães Rosa']
livro = ['A arte da Guerra','Poesias selecionadas','A montanha mágica','Primeiras estórias']
ano = [2000,2004,2015,2017]


# Criação do dicionário que estrutura os dados em formato de colunas
dados_livro = {'Autor':autor, 'Livro':livro, 'Ano':ano}
print(dados_livro)


# Conversão do dicionário em um DataFrame do Pandas (tabela)
autores = pd.DataFrame(dados_livro)
print(autores)


# Exportação dos dados do DataFrame para um arquivo CSV chamado 'livraria.csv'
autores.to_csv('livraria.csv')