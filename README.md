📊 Dashboard de Segurança Pública – RJ

Este projeto é um dashboard interativo desenvolvido em Python + Streamlit, utilizando dados do CISP para analisar criminalidade no estado do Rio de Janeiro.
O objetivo é fornecer visualizações claras sobre homicídios, roubos, furtos e total de crimes por região e ano.

🚀 Principais funcionalidades

✔️ Filtros por ano e região
✔️ Indicadores (cards) com totais de cada crime
✔️ Gráfico linha de homicídios por ano
✔️ Gráfico barra comparando regiões
✔️ Gráfico área de roubos ao longo dos anos
✔️ Ranking das regiões mais perigosas
✔️ Mapa interativo com intensidade de crimes (Mapbox)
✔️ Tabela detalhada dos dados filtrados

🛠️ Tecnologias utilizadas

Python
Streamlit
Pandas
Plotly Express
OpenPyXL (para leitura do Excel)

📦 Estrutura do Projeto
Dashboard_Cisp/
│
├── BaseDadosCisp.xlsx        # Base original do CISP
├── dashboard.py              # Aplicação Streamlit (principal)
├── requirements.txt          # Dependências
└── README.md                 # Documentação

📍 Sobre a base de dados

. A base contém os campos:

. ano

. regiao (Capital, Baixada Fluminense, Niteroi, Interior)

. hom_doloso

. total_roubos

. total_furtos

 O código calcula automaticamente:

. crime_total

. Coordenadas geográficas para visualização no mapa
