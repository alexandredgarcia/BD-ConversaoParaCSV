# 📚 Livraria 

Este projeto foi desenvolvido em Python com o objetivo de demonstrar como estruturar dados utilizando listas e dicionários, convertê-los para um DataFrame com a biblioteca Pandas e exportá-los para um arquivo no formato CSV.
O projeto faz parte dos meus estudos em desenvolvimento Python e tem como foco a prática de manipulação de dados e geração de arquivos.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Pandas** (Biblioteca para manipulação e análise de dados)

---

## 🚀 Funcionalidades
- Criação de listas contendo autores, livros e anos de publicação.
- Organização das informações em um dicionário.
- Conversão dos dados para um DataFrame utilizando Pandas.
- Exportação dos dados para um arquivo livraria.csv.

---

## 📂 Estrutura do projeto
```text
livraria-csv/
│
├── main.py
├── livraria.csv
└── README.md
```

---

## 📝 Exemplo do Código

import pandas as pd

# Dados de exemplo
autor = ['Sun Tzu','Fernando Pessoa','Thomaz Mann','João Guimarães Rosa']
livro = ['A arte da Guerra','Poesias selecionadas','A montanha mágica','Primeiras estórias']
ano = [2000,2004,2015,2017]

# Criando o DataFrame e exportando para CSV
dados_livro = {'Autor': autor, 'Livro': livro, 'Ano': ano}
autores = pd.DataFrame(dados_livro)
autores.to_csv('livraria.csv')

---

## 📊 Exemplo de saída
Dados exibidos no console
```text
Autor	                Livro  	                Ano
Sun Tzu	              A Arte da Guerra  	    2000
Fernando Pessoa	      Poesias Selecionadas    2004
Thomaz Mann	          A Montanha Mágica	      2015
João Guimarães Rosa	  Primeiras Estórias    	2017
```

---

## 📄 Arquivo gerado

Após a execução será criado o arquivo:

livraria.csv

contendo os dados organizados em formato tabular.

---

👤 Autor: Desenvolvido por Alexandre Dias Garcia

Aspirante em Desenvolvimento Python

🧑‍💻 Alexandre Dias Garcia 🔗 https://www.linkedin.com/in/alexandred-garcia

📧 alexandredgarcia23@gmail.com
