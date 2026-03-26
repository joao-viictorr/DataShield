# DataShield
Projeto educacional, tem como proposta anonimização de dados de um dataset.

## Descrição do Projeto
Este projeto tem como objetivo aplicar técnicas de **anonimização e pseudonimização** em um conjunto de dados reais, utilizando como base um dataset público contendo informações sobre gastos de parlamentares. A proposta está alinhada ao objetivo geral da disciplina, que consiste em demonstrar a compreensão dos conceitos teóricos por meio de sua aplicação prática, bem como justificar as escolhas realizadas durante o processo.

No contexto acadêmico, o foco do trabalho não está na criação de algoritmos complexos ou automatizados para anonimização, mas sim na **análise do conjunto de dados** e na aplicação consciente de técnicas adequadas para proteger informações sensíveis. A partir dessa análise, o dataset é tratado e modificado utilizando Python, garantindo que os dados pessoais sejam preservados sem comprometer a utilidade das informações.

O fluxo do projeto inicia com a leitura de um arquivo `.csv` contendo um grande volume de dados. Em seguida, é realizado um filtro temporal para isolar apenas os registros do ano de 2020. Após essa etapa, são aplicadas diferentes técnicas de anonimização:

- **Pseudonimização de parlamentares:** os nomes são substituídos por identificadores únicos (como P001, P002, etc.), garantindo consistência ao longo do dataset.
- **Generalização de dados geográficos:** os estados (UF) são agrupados por região, reduzindo o nível de detalhamento das informações.
- **Remoção de dados irrelevantes:** campos considerados desnecessários para a análise final são descartados.

Todo esse processamento é centralizado em uma função principal, que otimiza a leitura do arquivo e aplica todas as transformações em uma única passagem pelos dados. Ao final, os dados tratados são estruturados e exportados novamente no formato `.csv`.

Em termos de implementação, o projeto utiliza **Python**, com apoio da biblioteca pandas para manipulação de dados, além de módulos nativos como `csv` e `os`.

## Funcionalidades
O sistema foi desenvolvido para realizar o processamento e a anonimização de um conjunto de dados a partir de um fluxo estruturado de etapas. A entrada do sistema consiste em um arquivo `.csv` contendo um grande volume de dados relacionados aos gastos de parlamentares.

Inicialmente, é aplicado um filtro temporal por meio da função `data_filter`, que gera um novo arquivo `.csv` contendo apenas os registros referentes ao ano de 2020. Essa etapa reduz o volume de dados e delimita o escopo da análise.

Após o pré-processamento, são aplicadas as técnicas de anonimização:

- `anonimizar_parlamentar(nome)`: Responsável pela pseudonimização dos parlamentares. A função substitui os nomes reais por identificadores únicos e consistentes, como `P001`, `P002`, `P003`, garantindo que um mesmo parlamentar mantenha sempre o mesmo identificador ao longo do dataset.
- `anonimizar_estado(uf)`: Aplica a técnica de generalização aos dados geográficos. Utilizando um dicionário que relaciona estados às suas respectivas regiões, a função substitui a sigla do estado (UF) pela região correspondente, reduzindo o nível de detalhamento da informação.

A função principal, `processar_csv(caminho_csv)`, centraliza toda a lógica do sistema. É responsável por:
Ler o arquivo de entrada;
Remover campos considerados desnecessários;
Aplicar as funções de anonimização definidas anteriormente;
Garantir que todo o processamento seja feito em uma única leitura do arquivo, otimizando o desempenho.

Por fim, a função `salvar_csv_anonimizado(lista_dados, caminho_saida)` recebe os dados já processados (estruturados como uma lista de dicionários) e os converte novamente para o formato `.csv`, gerando o arquivo final anonimizado.