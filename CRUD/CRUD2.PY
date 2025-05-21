import mysql.connector
from mysql.connector import Error

# ✅ Conexão
def conectar():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="WebDrive"
        )
        if connection.is_connected():
            print("✅ Conectado ao banco WebDrive.")
            return connection
    except Error as e:
        print("❌ Erro ao conectar:", e)
    return None

# ✅ Funções CRUD genéricas
def inserir(connection, tabela):
    cursor = connection.cursor()
    colunas = input(f"Digite as colunas separadas por vírgula para a tabela {tabela}: ")
    valores = input(f"Digite os valores separados por vírgula: ")

    colunas_lista = [col.strip() for col in colunas.split(",")]
    valores_lista = [val.strip() for val in valores.split(",")]

    placeholders = ', '.join(['%s'] * len(valores_lista))
    sql = f"INSERT INTO {tabela} ({', '.join(colunas_lista)}) VALUES ({placeholders})"

    try:
        cursor.execute(sql, valores_lista)
        connection.commit()
        print(f"✅ Registro inserido na tabela {tabela}.")
    except Error as e:
        print(f"❌ Erro ao inserir na tabela {tabela}:", e)

def ler(connection, tabela):
    cursor = connection.cursor()
    sql = f"SELECT * FROM {tabela}"

    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(f"📋 Registros da tabela {tabela}:")
        for linha in resultados:
            print(linha)
    except Error as e:
        print(f"❌ Erro ao ler tabela {tabela}:", e)

def atualizar(connection, tabela):
    cursor = connection.cursor()
    coluna_alvo = input("Digite o nome da coluna que quer atualizar: ")
    novo_valor = input("Digite o novo valor: ")
    coluna_cond = input("Digite a coluna da condição (ex: id): ")
    valor_cond = input("Digite o valor da condição: ")

    sql = f"UPDATE {tabela} SET {coluna_alvo} = %s WHERE {coluna_cond} = %s"

    try:
        cursor.execute(sql, (novo_valor, valor_cond))
        connection.commit()
        print(f"✅ Registro atualizado na tabela {tabela}.")
    except Error as e:
        print(f"❌ Erro ao atualizar tabela {tabela}:", e)

def excluir(connection, tabela):
    cursor = connection.cursor()
    coluna_cond = input("Digite a coluna da condição (ex: id): ")
    valor_cond = input("Digite o valor da condição: ")

    sql = f"DELETE FROM {tabela} WHERE {coluna_cond} = %s"

    try:
        cursor.execute(sql, (valor_cond,))
        connection.commit()
        print(f"✅ Registro excluído da tabela {tabela}.")
    except Error as e:
        print(f"❌ Erro ao excluir da tabela {tabela}:", e)

# ✅ CRUD de cada tabela
def crud_usuarios(connection):
    while True:
        print("\n--- CRUD USUÁRIOS ---")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            inserir(connection, "usuarios")
        elif op == "2":
            ler(connection, "usuarios")
        elif op == "3":
            atualizar(connection, "usuarios")
        elif op == "4":
            excluir(connection, "usuarios")
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

def crud_arquivos(connection):
    while True:
        print("\n--- CRUD ARQUIVOS ---")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            inserir(connection, "arquivos")
        elif op == "2":
            ler(connection, "arquivos")
        elif op == "3":
            atualizar(connection, "arquivos")
        elif op == "4":
            excluir(connection, "arquivos")
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

def crud_instituicoes(connection):
    while True:
        print("\n--- CRUD INSTITUIÇÕES ---")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            inserir(connection, "instituicoes")
        elif op == "2":
            ler(connection, "instituicoes")
        elif op == "3":
            atualizar(connection, "instituicoes")
        elif op == "4":
            excluir(connection, "instituicoes")
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

def crud_planos(connection):
    while True:
        print("\n--- CRUD PLANOS ---")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            inserir(connection, "planos")
        elif op == "2":
            ler(connection, "planos")
        elif op == "3":
            atualizar(connection, "planos")
        elif op == "4":
            excluir(connection, "planos")
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

def crud_suporte(connection):
    while True:
        print("\n--- CRUD SUPORTE ---")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            inserir(connection, "suporte")
        elif op == "2":
            ler(connection, "suporte")
        elif op == "3":
            atualizar(connection, "suporte")
        elif op == "4":
            excluir(connection, "suporte")
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

def crud_versionamento(connection):
    while True:
        print("\n--- CRUD VERSIONAMENTO ---")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            inserir(connection, "versionamento")
        elif op == "2":
            ler(connection, "versionamento")
        elif op == "3":
            atualizar(connection, "versionamento")
        elif op == "4":
            excluir(connection, "versionamento")
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

# ✅ Menu principal
def main():
    connection = conectar()
    if not connection:
        return

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - CRUD Usuários")
        print("2 - CRUD Arquivos")
        print("3 - CRUD Instituições")
        print("4 - CRUD Planos")
        print("5 - CRUD Suporte")
        print("6 - CRUD Versionamento")
        print("0 - Sair")

        op = input("Escolha uma tabela para mexer: ")

        if op == "1":
            crud_usuarios(connection)
        elif op == "2":
            crud_arquivos(connection)
        elif op == "3":
            crud_instituicoes(connection)
        elif op == "4":
            crud_planos(connection)
        elif op == "5":
            crud_suporte(connection)
        elif op == "6":
            crud_versionamento(connection)
        elif op == "0":
            break
        else:
            print("❌ Opção inválida.")

    connection.close()
    print("✅ Conexão encerrada.")

if __name__ == "__main__":
    main()
