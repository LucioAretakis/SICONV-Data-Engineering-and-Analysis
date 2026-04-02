## 📑 Automação de Relatórios em PDF (`generate_report.py`)

Este módulo é responsável por extrair dados financeiros do banco de dados, gerar visualizações gráficas e consolidar as informações em um relatório técnico em formato PDF de forma 100% automatizada.

### 🚀 Funcionalidades
* **Extração SQL Dinâmica:** Conecta-se ao PostgreSQL e realiza o `JOIN` entre as tabelas de execução financeira e convênios para consolidar repasses por data.
* **Processamento de Dados:** Utiliza **Pandas** para limpeza e agrupamento temporal (anualização dos dados).
* **Data Viz:** Gera gráficos de barras customizados com **Matplotlib**, incluindo rótulos de dados formatados em moeda (BRL).
* **Engine de PDF:** Utiliza a biblioteca **PyFPDF** para criar um layout personalizado com cabeçalho (logo), rodapé e blocos de observações técnicas.

---

### 🛠️ Tecnologias e Bibliotecas
* **Python 3.x**
* **Pandas:** Manipulação e agregação de dados.
* **SQLAlchemy / Psycopg2:** Interface de conexão com o banco de dados.
* **Matplotlib:** Geração do gráfico de evolução anual.
* **FPDF:** Construção da estrutura do documento PDF.

---

### 📋 Pré-requisitos
Antes de executar, certifique-se de ter as dependências instaladas:

```bash
pip install matplotlib pandas fpdf sqlalchemy psycopg2
