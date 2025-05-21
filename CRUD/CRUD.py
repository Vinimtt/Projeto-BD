import mysql.connector
from mysql.connector import Error

# ✅ Função para conectar ao banco
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

# ✅ Função genérica para inserção
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

# ✅ Função genérica para leitura
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

# ✅ Função genérica para atualização
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

# ✅ Função genérica para exclusão
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

# ✅ Menu principal
def main():
    connection = conectar()
    if not connection:
        return

    while True:
        print("\n===== MENU CRUD WebDrive =====")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        tabela = input("Digite o nome da tabela: ")

        if opcao == "1":
            inserir(connection, tabela)
        elif opcao == "2":
            ler(connection, tabela)
        elif opcao == "3":
            atualizar(connection, tabela)
        elif opcao == "4":
            excluir(connection, tabela)
        else:
            print("❌ Opção inválida.")

    connection.close()
    print("✅ Conexão encerrada.")

if __name__ == "__main__":
    main()
