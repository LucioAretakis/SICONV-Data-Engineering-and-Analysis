# ⚙️ Pipeline ETL - Processamento de Dados SICONV

Este repositório contém a camada de extração, tratamento e carga (ETL) desenvolvida no **Pentaho Data Integration (PDI)**. O objetivo deste projeto é automatizar a ingestão de dados brutos do repositório oficial do governo para um banco de dados estruturado, garantindo a integridade e a limpeza das informações de convênios.

---

## 🏗️ Estrutura do Projeto (Pentaho)

A solução está dividida em um Job principal de orquestração e múltiplas transformações especializadas:

### 1. Orquestração (`.kjb`)
* **`2ª etapa desafio técnico.kjb`**: O "cérebro" do pipeline. Este Job gerencia a ordem de execução, o controle de erros e a conexão entre a extração e as cargas subsequentes.

### 2. Extração e Tratamento (`.ktr`)
As transformações realizam o mapeamento dos campos, a normalização de tipos de dados e o carregamento nas tabelas de destino:

* **`Extração de repositório.ktr`**: Responsável por ler os arquivos CSV originais e preparar a base para o tratamento.
* **`Tratamento e carga - Proponentes.ktr`**: Processa e carrega os dados das entidades que propõem os convênios.
* **`Tratamento e carga - Convênios.ktr`**: Processa as informações detalhadas dos instrumentos de repasse.
* **`Tratamento e carga - Execução Financeira.ktr`**: Foca nos indicadores de valores pagos e percentuais de execução.
* **`Tratamento e carga - Situação.ktr`**: Carrega o histórico de status e situações dos convênios.

---

## 🚀 Fluxo de Execução

1. **Início:** O Job principal é disparado.
2. **Extração:** Os arquivos são baixados/lidos do repositório.
3. **Carga em Paralelo/Sequencial:** O Pentaho executa as transformações de carga respeitando a integridade referencial (carregando proponentes e convênios antes das tabelas de histórico/execução).
4. **Finalização:** Log de sucesso ou alerta em caso de falha em qualquer etapa.

---

## 🛠️ Tecnologias Utilizadas
* **Ferramenta ETL:** Pentaho Data Integration (Spoon) 9.x+
* **Origem dos Dados:** CSV (Repositório de Dados Abertos)
* **Destino:** PostgreSQL (Camada Silver/Gold)

---

## 📋 Pré-requisitos
* Ter o **PDI (Kettle)** instalado e configurado.
* Driver JDBC do **PostgreSQL** (`postgresql-42.x.jar`) na pasta `lib` do seu Pentaho.
* Variáveis de ambiente de banco de dados configuradas no arquivo `kettle.properties`.

---

## 🛡️ Destaques Técnicos
* **Automação Total:** Elimina a necessidade de carregamento manual de planilhas.
* **Padronização:** Limpeza de strings, tratamento de valores nulos e conversão de formatos de data brasileiros para o padrão ISO.
* **Escalabilidade:** Estrutura modular que permite adicionar novas tabelas de carga facilmente.
