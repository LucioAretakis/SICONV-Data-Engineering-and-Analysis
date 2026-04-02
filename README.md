# 📊 Análise de dados do SICONV

O cliente deseja visualizar e analisar dados referentes a convênios operacionalizados por meio do Sistema de Gestão de Convênios e Contratos de Repasse – SICONV. Os dados estão disponíveis publicamente em formato CSV no repositório oficial do governo: [https://repositorio.dados.gov.br/seges/detru/](https://repositorio.dados.gov.br/seges/detru/)

<img width="1283" height="719" alt="Captura de tela 2026-04-01 180438" src="https://github.com/user-attachments/assets/f22b7ac0-3e84-4bf6-822e-978af5a72f97" />


---

## 📁 Estrutura do Repositório

### 📂 Bases Utilizadas
Contém os arquivos de dados brutos extraídos do repositório original. Estes arquivos servem como a *Single Source of Truth* (Fonte Única de Verdade) para o carregamento inicial no PostgreSQL.

### 📂 CRUD CLI
Interface de linha de comando desenvolvida em Python para gerenciamento do banco de dados.
* **Funcionalidades:** Criação de registros, consultas dinâmicas e manutenção de dados.
* **Documentação:** Veja o `README.md` interno para instruções de configuração e comandos.

### 📂 ETL (Pentaho Data Integration)
Coração do processamento de dados, contendo arquivos `.ktr` (Transformações) e `.kjb` (Jobs).
* **Fluxo:** Orquestração da limpeza, padronização e carga (Load) no banco de dados.
* **Destaque:** Automatização da esteira de dados garantindo integridade e performance.

### 📂 PostgreSQL
Documentação da arquitetura de dados em nível de servidor.
* **Conteúdo:** Script `.sql` completo com DDL (Data Definition Language).
* **Diferenciais:** Inclui criação de índices para otimização de *queries* e documentação de relacionamentos (FKs) via comentários no código.

### 📂 Power BI
Camada de Inteligência de Negócio para suporte à decisão.
* **Arquivo:** `.pbix` com dashboard interativo.
* **Foco:** Visualizações estratégicas, cálculos de indicadores (DAX) e análise de tendências.

---

## 🚀 Scripts de Automação

### 📄 `generate_report.py`
Script especializado em *Data Visualization as Code*.
* Conecta-se diretamente ao PostgreSQL.
* Gera gráficos estatísticos de forma programática.
* Exporta relatórios automatizados, eliminando processos manuais de *reporting*.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
| :--- | :--- |
| **Linguagem** | Python 3.x |
| **ETL** | Pentaho Data Integration (PDI) |
| **Banco de Dados** | PostgreSQL |
| **Visualização** | Power BI & Matplotlib/Seaborn |
| **IDE** | VS Code / DBeaver |
