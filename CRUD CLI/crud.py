import psycopg2
import sys
from connection import db_pass

# Configura parâmetros do banco de dados
def conectar():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password= db_pass,
            host='localhost',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro de conexão com o banco: {e}")
        sys.exit(1)

def criar_convenio(): 
    nr_convenio = int(input("Número do convênio: "))
    dia_assin = input("Dia da assinatura do contrato (DD/MM/yyyy): ")
    fim_vigenc = input("Fim da vigência do convênio: ")
    dia_limite = input("Dia limite para prestação de contas: ")
    nr_processo = input("Insira o número do processo: ")
    sit_convenio = input("Situação atual do convênio: ")

    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute("""
                    
                    INSERT INTO convenios (nr_convenio, dia_assin_conv, dia_inic_vigen_conv, dia_fim_vigenc_conv, sit_convenio, dia_limite_prest_contas) 
                    VALUES (%s,%s,%s,%s,%s,%s)
                    """, (nr_convenio, dia_assin, dia_assin, fim_vigenc, dia_limite, nr_processo, sit_convenio))
        conn.commit()
        print("Novo convênio criado com sucesso, todos os dados foram adicionados à base.")
    except Exception as e:
        print(f'Erro ao criar convênio: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def listar_convenios(): # Mecanismo de listagem de convênios existentes
    
    nr_conv = input('Insira o número do convênio que deseja listar (Pressione Enter e deixe vazio caso deseja listar todos): ')
    
    conn = conectar()
    cur = conn.cursor()
    
    try: 
            if nr_conv.strip():
                cur.execute("SELECT * FROM convenios WHERE nr_convenio = %s", (nr_conv,))
            else:
                cur.execute("SELECT * FROM convenios")
            convenios = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            if convenios:
                print(" | ".join(colnames))
                for c in convenios:
                    print( "| ".join(str(item) for item in c))
            else:
                print("Nenhum convênio encontrado.")
    except Exception as e:
        print(f'Erro ao listar convênios: {e}')
    finally:
        cur.close()
        conn.close()

def atualizar_convenio(): # Atualizando convênios

    nr_convenio = input("Número do convênio a atualizar: ")
    sit_conv = input("Novo status do convênio: ")
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute("UPDATE convenios SET sit_convenio = %s WHERE nr_convenio = %s", (sit_conv, nr_convenio))
        if cur.rowcount():
            conn.commit()
            print("Convenio atualizado com sucesso")
        else:
            print("Convenio não encontrado")
    except Exception as e:
        print(f'Erro ao atualizar convênio: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def excluir_convenio(): # Excluindo convênios
    nr_convenio = input("Número do convênio a excluir: ")
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM convenios WHERE nr_convenio = %s", (nr_convenio,))
        if cur.rowcount:
            conn.commit()
            print("Convênio excluído com sucesso")
        else:
            print("Convênio não encontrado")
    except Exception as e:
        print(f'Erro ao excluir convênio: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def menu():
    while True:
        print("\n==== Menu CRUD Convênios ====")
        print("1. Criar novo convênio")
        print("2. Listar convênios")
        print("3. Atualizar convênio")
        print("4. Excluir convênio")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_convenio()
        elif escolha == '2':
            listar_convenios()
        elif escolha == '3':
            atualizar_convenio()
        elif escolha == '4':
            excluir_convenio()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
