# 🗄️ Arquitetura de Dados - Sistema SICONV

Este repositório contém as definições de estrutura de dados (DDL) para o monitoramento e análise de convênios do governo federal (SICONV). O esquema foi projetado para suportar consultas complexas de business intelligence, garantindo integridade referencial e alta performance.

---

## 📊 Estrutura das Tabelas

O banco de dados está dividido em quatro núcleos principais de informação, todos interconectados via `id_proposta`:

### 1. **Proponentes (Tabela Principal)**
Armazena os dados cadastrais das entidades proponentes, incluindo localização, informações bancárias e detalhes da proposta original.
* **Chave Primária:** `id_proposta`
* **Campos Relevantes:** `nm_proponente`, `vl_global_prop`, `uf_proponente`.

### 2. **Convênios**
Contém os dados detalhados da execução do instrumento, como datas de assinatura, publicação, vigência e saldos financeiros.
* **Foco Financeiro:** Rastreia valores empenhados, desembolsados e rendimentos de aplicação.

### 3. **Situação e Histórico**
Tabela de apoio que armazena o histórico de alterações de status de cada convênio.
* **Relacionamento:** Vinculada tanto a `proponentes` quanto a `convenios` via *Foreign Key*.

### 4. **Execução Financeira**
Camada de resumo físico-financeiro para análise de performance de projetos.
* **Indicador:** `percentual_execucao_resumo_fisico_financeiro`.

---

## 📍 Tabela de Localidades
Para otimização de consultas geográficas e normalização, foi criada uma tabela específica de **Localidades** derivada da tabela de proponentes. Isso facilita a criação de filtros por UF e Municípios em ferramentas de visualização como o Power BI.

---

## ⚡ Performance e Otimização

Para garantir que o dashboard e as consultas SQL sejam rápidos, foram implementados **Índices Pós-Carga** nos campos de busca mais frequentes:

| Tabela | Índice | Campo Indexado | Motivo |
| :--- | :--- | :--- | :--- |
| **Localidades** | `idx_localidades_cod_munic` | `cod_munic_ibge` | Agilidade em JOINS geográficos. |
| **Localidades** | `idx_uf` | `uf_proponente` | Performance em filtros de estado. |
| **Convênios** | `idx_convenios_nr_convenio` | `nr_convenio` | Busca rápida por número de contrato. |
| **Situação** | `idx_situacao_id_proposta` | `id_proposta` | Integridade e velocidade no histórico. |

---

## 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** PostgreSQL
* **Linguagem:** SQL (DDL e DML)
* **Conceitos Aplicados:** Índices B-Tree, Chaves Estrangeiras (FK), Normalização de Dados e Criação de Tabelas via Select (CTAS).

---

## 🚀 Como Implantar
1. Certifique-se de que o servidor **PostgreSQL** está em execução.
2. Execute os scripts na ordem numérica definida no arquivo `.sql` (1 a 4) para garantir que as dependências de chaves estrangeiras sejam respeitadas.
3. Após a carga dos dados, execute os comandos de **Criação de Índices** para otimizar o ambiente.
