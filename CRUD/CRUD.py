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

# ✅ Submenu de operações
def submenu(connection, tabela):
    while True:
        print(f"\n===== OPERACOES TABELA {tabela.upper()} =====")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir(connection, tabela)
        elif opcao == "2":
            ler(connection, tabela)
        elif opcao == "3":
            atualizar(connection, tabela)
        elif opcao == "4":
            excluir(connection, tabela)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")

# ✅ Menu principal
def main():
    connection = conectar()
    if not connection:
        return

    while True:
        print("\n===== MENU PRINCIPAL WebDrive =====")
        print("Escolha a tabela para mexer:")
        print("1 - usuarios")
        print("2 - arquivos")
        print("3 - instituicoes")
        print("4 - planos")
        print("5 - suporte")
        print("6 - versionamento")
        print("0 - Sair")

        tabela_opcao = input("Escolha uma opção: ")

        if tabela_opcao == "1":
            submenu(connection, "usuarios")
        elif tabela_opcao == "2":
            submenu(connection, "arquivos")
        elif tabela_opcao == "3":
            submenu(connection, "instituicoes")
        elif tabela_opcao == "4":
            submenu(connection, "planos")
        elif tabela_opcao == "5":
            submenu(connection, "suporte")
        elif tabela_opcao == "6":
            submenu(connection, "versionamento")
        elif tabela_opcao == "0":
            break
        else:
            print("❌ Opção inválida.")

    connection.close()
    print("✅ Conexão encerrada.")

if __name__ == "__main__":
    main()
