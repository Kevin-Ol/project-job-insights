# Projeto Job Insights

Projeto feito como critério avaliativo na escola de programação Trybe.

Foi utilizada a linguagem de programação Python.

O objetivo do projeto foi consolidar o conhecimento na leitura e manipulação de dados de um arquivo csv, fazendo buscas por valores únicos, filtros, 
máximos, mínimos e testes simples.

## Instruções para reproduzir o projeto

#### Pré Requisitos

Possuir Python instalado

---

1. Clone o repositório
  * `git@github.com:Kevin-Ol/project-job-insights.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    * `cd project-job-insights`

2. Inicie e ative um ambiente virtual
  * `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências
  * `python3 -m pip install -r dev-requirements.txt`

---

As funções desenvolvidas no projeto são:

`jobs.py`

- Função `read`: possui como parâmetro o caminho do arquivo e é responsável por retornar uma lista de dicionários referente aos 
dados do arquivo csv;

`insights.py`

- Função `get_unique_job_types`: possui como parâmetro o caminho do arquivo e é responsável por retornar uma lista contendo os tipos de emprego contidos no 
arquivo;

- Função `filter_by_job_type`: possui como parâmetros a lista de empregos e o tipo de emprego buscado, e é responsável por retornar uma lista 
contendo os empregos correspondentes ao tipo escolhido;

- Função `get_unique_industries`: possui como parâmetro o caminho do arquivo e é responsável por retornar uma lista contendo os nomes das empresas contidos no 
arquivo;

- Função `filter_by_industry`: possui como parâmetros a lista de empresas e o nome da empresa buscada, e é responsável por retornar uma lista 
contendo os empregos correspondentes à empresa escolhida;

- Função `get_max_salary`: possui como parâmetro o caminho do arquivo e é responsável por retornar o maior salário contido no arquivo;

- Função `get_min_salary`: possui como parâmetro o caminho do arquivo e é responsável por retornar o menor salário contido no arquivo;

- Função `matches_salary_range`: possui como parâmetro um emprego e um salário, e é responsável por retornar um valor booleano indicando se o salário 
informado está entre o salário mínimo e o salário máximo para aquela vaga. Também retorna um erro caso algum dos dados do emprego esteja faltando ou 
seja inválido;

- Função `filter_by_salary_range`: possui como parâmetros uma lista de empregos e um salário, e é responsável por retornar uma lista de empregos 
correspondentes ao salário informado, usando `matches_salary_range` como função auxiliar;

`test_sorting.py`

- Foram desenvolvidos testes simples para as funções contidas no arquivo `sorting.py`;
