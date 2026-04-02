```Markdown
# 🖥️ CRUD CLI - Gestão de Convênios

Esta é uma interface de linha de comando desenvolvida em Python para realizar operações de manutenção diretamente no banco de dados **PostgreSQL**. O sistema permite o ciclo completo de gerenciamento de dados (*Create, Read, Update, Delete*) de forma segura e interativa.

---

## 🛠️ Funcionalidades
O script oferece um menu interativo com as seguintes capacidades:

* **Criar novo convênio:** Cadastro completo incluindo número do convênio, datas de vigência, número do processo e situação atual.
* **Listar convênios:** Consulta flexível que permite visualizar um registro específico (por número) ou listar todos os itens da base.
* **Atualizar convênio:** Permite alterar o status/situação de um convênio existente.
* **Excluir convênio:** Remoção lógica/física de registros através do identificador único.

---

## 🏗️ Arquitetura Técnica
* **Linguagem:** Python 3.x
* **Driver de Banco:** `psycopg2` (utilizado para comunicação de baixa latência com o PostgreSQL).
* **Segurança:** Utiliza **Parameterized Queries** (consultas parametrizadas) para prevenir ataques de *SQL Injection*.
* **Gestão de Estado:** Implementa controle de transações com `commit()` e `rollback()` para garantir a integridade dos dados em caso de falhas.

---

## 🚀 Como Utilizar

### Pré-requisitos
Certifique-se de que o arquivo `connection.py` está no mesmo diretório e contém a variável `db_pass`.

```python
# connection.py
db_pass = "sua_senha_aqui"


### Execução
1. Abra o terminal na pasta do projeto.
2. Execute o comando:
```bash
python crud_cli.py

3. Siga as instruções numeradas no menu interativo.

---

## 🛡️ Tratamento de Erros e Resiliência

O sistema está preparado para lidar com diversas situações adversas:

### 🔌 Falhas de Conexão

Status: Erro de Conexão
Ação: O script encerra a execução com uma mensagem clara caso o banco de dados 
      esteja offline ou as credenciais estejam incorretas.


### 🔄 Transações Interrompidas (Rollback)

Status: Falha na Operação SQL
Ação: Em caso de erro durante a inserção ou exclusão, o sistema realiza um 
      rollback automático, garantindo que a consistência do banco não seja afetada.


### 📝 Validação de Entrada

Status: Dado Inválido Detectado
Ação: Tratamento para garantir que tipos de dados (como números de convênio e 
      datas) sejam processados corretamente antes de chegarem ao banco.

```

