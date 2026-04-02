# 🖥️ CRUD CLI - Gestão de Convênios

Esta é uma interface de linha de comando desenvolvida em **Python** para realizar operações de manutenção diretamente no banco de dados **PostgreSQL**. O sistema permite o ciclo completo de gerenciamento de dados (**Create, Read, Update, Delete**) de forma segura e interativa.

---

## 🛠️ Funcionalidades

O script oferece um menu interativo com as seguintes capacidades:

- **Criar novo convênio**  
  Cadastro completo incluindo número do convênio, datas de vigência, número do processo e situação atual.

- **Listar convênios**  
  Consulta flexível que permite visualizar um registro específico (por número) ou listar todos os itens da base.

- **Atualizar convênio**  
  Permite alterar o status/situação de um convênio existente.

- **Excluir convênio**  
  Remoção lógica/física de registros através do identificador único.

---

## 🏗️ Arquitetura Técnica

- **Linguagem:** Python 3.x  
- **Driver de Banco:** `psycopg2` (utilizado para comunicação de baixa latência com o PostgreSQL)  
- **Segurança:** Utiliza *Parameterized Queries* (consultas parametrizadas) para prevenir ataques de SQL Injection  
- **Gestão de Estado:** Implementa controle de transações com `commit()` e `rollback()` para garantir a integridade dos dados em caso de falhas  

---

## 🚀 Como Utilizar

### Pré-requisitos

Certifique-se de que o arquivo `connection.py` está no mesmo diretório e contém a variável `db_pass`:

# connection.py
db_pass = "sua_senha_aqui"

## 🛡️ Tratamento de Erros

O sistema está preparado para lidar com diferentes cenários de falha, garantindo a integridade dos dados e uma experiência segura para o usuário:

- **Falhas de Conexão**  
  Caso o banco de dados esteja offline ou inacessível, o sistema encerra a execução e exibe uma mensagem clara informando o problema.

- **Transações Interrompidas**  
  Se ocorrer algum erro durante operações como inserção, atualização ou exclusão, o sistema executa automaticamente um `rollback()`, desfazendo quaisquer alterações parciais e preservando a consistência dos dados.

- **Validação de Entrada**  
  O sistema realiza validações básicas nos dados informados pelo usuário (como números de convênio e campos obrigatórios), evitando erros de tipo e entradas inválidas.

- **Tratamento de Exceções**  
  Utiliza blocos `try/except` para capturar erros inesperados durante a execução, evitando que o programa seja interrompido abruptamente.

- **Mensagens de Feedback**  
  O usuário recebe mensagens informativas em caso de sucesso ou falha nas operações, facilitando a identificação e correção de problemas.
