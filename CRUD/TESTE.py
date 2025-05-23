import mysql.connector
from mysql.connector import Error

# Parte 1: Conectar, criar banco e tabelas, e inserir registros de teste
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  
    )

    if connection.is_connected():
        print("Conectado ao MySQL com sucesso!")
        cursor = connection.cursor()

        # Criar banco de dados
        cursor.execute("CREATE DATABASE IF NOT EXISTS WebDrive")
        cursor.execute("USE WebDrive")

        # Tabelas
        tabelas = [

            # Tabela plano
            """
            CREATE TABLE IF NOT EXISTS plano (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(100),
                duracao VARCHAR(100),
                data_aquisicao VARCHAR(100),
                espaco_usuario DOUBLE
            )
            """,

            # Tabela instituicao
            """
            CREATE TABLE IF NOT EXISTS instituicao (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(100),
                causa_social VARCHAR(100),
                endereco VARCHAR(100),
                id_plano INT,
                FOREIGN KEY (id_plano) REFERENCES plano(id)
            )
            """,

            # Tabela usuario
            """
            CREATE TABLE IF NOT EXISTS usuario (
                id INT PRIMARY KEY AUTO_INCREMENT,
                login VARCHAR(100),
                senha VARCHAR(100),
                email VARCHAR(100),
                data_ingresso VARCHAR(100),
                id_instituicao INT,
                FOREIGN KEY (id_instituicao) REFERENCES instituicao(id)
            )
            """,

            # Tabela arquivo
            """
            CREATE TABLE IF NOT EXISTS arquivo (
                id INT PRIMARY KEY AUTO_INCREMENT,
                data_de_ultima_alteracao VARCHAR(100),
                url VARCHAR(100),
                localizacao VARCHAR(100),
                permissao_de_acesso VARCHAR(100),
                nome VARCHAR(100),
                tipo VARCHAR(100),
                tamanho VARCHAR(100),
                id_usuario INT,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id)
            )
            """,

            # Tabela compartilhamento
            """
            CREATE TABLE IF NOT EXISTS compartilhamento (
                id_compartilhamento INT PRIMARY KEY AUTO_INCREMENT,
                data_compartilhamento VARCHAR(100),
                id_arquivo INT,
                id_user_send INT,
                id_user_receive INT,
                FOREIGN KEY (id_arquivo) REFERENCES arquivo(id),
                FOREIGN KEY (id_user_send) REFERENCES usuario(id),
                FOREIGN KEY (id_user_receive) REFERENCES usuario(id)
            )
            """,

            # Tabela comentario
            """
            CREATE TABLE IF NOT EXISTS comentario (
                id INT PRIMARY KEY AUTO_INCREMENT,
                conteudo VARCHAR(100),
                data VARCHAR(100),
                hora VARCHAR(100),
                id_usuario INT,
                id_arquivo INT,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
            )
            """,

            # Tabela historico_de_versionamento
            """
            CREATE TABLE IF NOT EXISTS historico_de_versionamento (
                id_historico INT PRIMARY KEY AUTO_INCREMENT,
                data VARCHAR(100),
                hora VARCHAR(100),
                operacao VARCHAR(100),
                id_usuario INT,
                id_usuario_que_alterou INT,
                conteudo_alterado VARCHAR(100),
                id_arquivo INT,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
            )
            """,

            # Tabela Admin
            """
            CREATE TABLE IF NOT EXISTS Admin (
                id INT PRIMARY KEY AUTO_INCREMENT,
                login VARCHAR(100),
                senha VARCHAR(100),
                email VARCHAR(100),
                data_ingresso VARCHAR(100)
            )
            """
        ]

        for comando in tabelas:
            cursor.execute(comando)

        print("Todas as tabelas foram criadas com sucesso no banco WebDrive!")

        # Inserir dados de teste em plano
        cursor.execute("INSERT INTO plano (nome, duracao, data_aquisicao, espaco_usuario) VALUES ('Plano Básico', '12 meses', '2025-01-01', 10.0)")

        # Inserir dados de teste em instituicao
        cursor.execute("INSERT INTO instituicao (nome, causa_social, endereco, id_plano) VALUES ('Instituto ABC', 'Educação', 'Rua X', 1)")

        # Inserir dados de teste em usuario
        cursor.execute("INSERT INTO usuario (login, senha, email, data_ingresso, id_instituicao) VALUES ('user1', '1234', 'user1@email.com', '2025-01-01', 1)")

        # Inserir dados de teste em arquivo
        cursor.execute("INSERT INTO arquivo (data_de_ultima_alteracao, url, localizacao, permissao_de_acesso, nome, tipo, tamanho, id_usuario) VALUES ('2025-01-01', 'http://arquivo.com', 'pasta1', 'privado', 'arquivo1', 'txt', '1KB', 1)")

        # Inserir dados de teste em compartilhamento
        cursor.execute("INSERT INTO compartilhamento (data_compartilhamento, id_arquivo, id_user_send, id_user_receive) VALUES ('2025-01-01', 1, 1, 1)")

        # Inserir dados de teste em comentario
        cursor.execute("INSERT INTO comentario (conteudo, data, hora, id_usuario, id_arquivo) VALUES ('Comentário teste', '2025-01-01', '10:00', 1, 1)")

        # Inserir dados de teste em historico_de_versionamento
        cursor.execute("INSERT INTO historico_de_versionamento (data, hora, operacao, id_usuario, id_usuario_que_alterou, conteudo_alterado, id_arquivo) VALUES ('2025-01-01', '10:00', 'Criação', 1, 1, 'Novo Conteúdo', 1)")

        # Inserir dados de teste em Admin
        cursor.execute("INSERT INTO Admin (login, senha, email, data_ingresso) VALUES ('admin', 'admin123', 'admin@webdrive.com', '2025-01-01')")

        connection.commit()
        print("Dados de teste inseridos com sucesso!")

except Error as e:
    print("Erro ao executar:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
        
        
        
def conectar():

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # Insira sua senha se estiver usando localmente
            database="WebDrive"
        )
        if connection.is_connected():
            print("Conectado ao banco WebDrive.")
            return connection
    except Error as e:
        print("Erro ao conectar:", e)
    return None

def inserir(connection, tabela):
    cursor = connection.cursor()

    # 1. Obter colunas
    try:
        cursor.execute(f"SELECT * FROM {tabela} LIMIT 0") # obtem metadados
        colunas = []
        # cursor.description retorna info. sobre as colunas
        for desc in cursor.description: 
            colunas.append(desc[0])
        cursor.fetchall()  # Limpa resultados pendentes do SELECT
    except Error as e:
        print(f"Ocorreu um erro em obter as colunas da tabela {tabela}: {e}")
        return

    # 2. Coletar dados do usuário
    valores = []
    print(f"\nInsira os valores para a tabela '{tabela}':")
    for col in colunas[1:]:  # Ignora a coluna 0 (PK auto_increment)
        valor = input(f"- {col}: ").strip()
        # Convertendo valores para int ou float caso precise
        if valor.isdigit():
            valor = int(valor)
        else:
            try:
                valor = float(valor)
            except ValueError:
                pass
        valores.append(valor) # Adiciona em valores[]

    # 3. Inserir no banco
    placeholders = ', '.join(['%s'] * len(valores))
    sql = f"INSERT INTO {tabela} ({', '.join(colunas[1:])}) VALUES ({placeholders})" # codigo 'em sql' para inserir

    try:
        cursor.execute(sql, valores)
        connection.commit()
        print(f"\nRegistro inserido com sucesso na tabela '{tabela}'.")
    except Error as e:
        print(f"Ocorreu um erro na inserção da tabela {tabela}: {e}")


def ler(connection, tabela):

    cursor = connection.cursor()
    sql = f"SELECT * FROM {tabela}"

    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()

        # Obtem os nomes das colunas
        colunas = [desc[0] for desc in cursor.description]

        print(f"\n📋 Registros da tabela {tabela}:\n")
        print(" | ".join(colunas))  # Imprime cabeçalho com separador

        for linha in resultados:
            print(" | ".join(str(campo) for campo in linha))

    except Error as e:
        print(f"Erro ao ler tabela {tabela}:", e)



def excluir(connection, tabela):
    cursor = connection.cursor()

    # 1. Obter colunas da tabela
    try:
        cursor.execute(f"SELECT * FROM {tabela} LIMIT 0")  # obtém metadados
        colunas = []
        for desc in cursor.description:
            colunas.append(desc[0])
        cursor.fetchall()  # limpa resultados
    except Error as e:
        print(f"Ocorreu um erro ao obter as colunas da tabela {tabela}: {e}")
        return

    # 2. Mostrar colunas disponíveis
    print(f"\nColunas disponíveis na tabela '{tabela}': {', '.join(colunas)}")

    # 3. Coletar coluna de condição e valor
    coluna_cond = input("Digite a coluna da condição para exclusão (ex: id): ").strip()
    if coluna_cond not in colunas:
        print(f" Coluna '{coluna_cond}' não existe na tabela '{tabela}'.")
        return

    valor_cond = input(f"Digite o valor da condição para '{coluna_cond}': ").strip()
    if valor_cond.isdigit():
        valor_cond = int(valor_cond)
    else:
        try:
            valor_cond = float(valor_cond)
        except ValueError:
            pass

    # 4. Montar e executar o DELETE
    sql = f"DELETE FROM {tabela} WHERE {coluna_cond} = %s"

    try:
        cursor.execute(sql, (valor_cond,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"\n Registro excluído com sucesso da tabela '{tabela}'.")
        else:
            print(f"\n Nenhum registro foi excluído da tabela '{tabela}'.")
    except Error as e:
        print(f"Ocorreu um erro ao excluir da tabela {tabela}: {e}")


# Submenu de operações
def submenu(connection, tabela):

    while True:
        print(f"\n===== OPERACOES TABELA {tabela.upper()} =====\n")
        print("1 - Inserir")
        print("2 - Ler")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar ao menu principal")
        print("\n==============================================\n")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                inserir(connection, tabela)
            case '2':
                ler(connection, tabela)
            case '3':
                atualizar(connection, tabela)
            case '4':
                excluir(connection, tabela)
            case '0':
                break
            case _:
                print("Opção inválida.")

#Menu principal
def main():

    connection = conectar()
    if not connection:
        return

    while True:
        print("\n===== MENU PRINCIPAL WebDrive =====\n")
        print("Escolha a tabela para operar:")
        print("1 - Admin")
        print("2 - Arquivo")
        print("3 - Comentário")
        print("4 - Compartilhamento")
        print("5 - Histórico de versionameto")
        print("6 - Instituição")
        print("7 - Plano")
        print("8 - Possui")
        print("9 - Usuários")
        print("0 - Sair")
        print("\n===================================\n")
        tabela_opcao = input("Escolha uma opção: ")

        match tabela_opcao:
            case '1':
                ler(connection, "admin")
                submenu(connection, "admin")
            case '2':
                ler(connection, "arquivo")
                submenu(connection, "arquivo")
            case '3':
                ler(connection, "comentario")
                submenu(connection, "comentario")
            case '4':
                ler(connection, "compartilhamento")
                submenu(connection, "compartilhamento")
            case '5':
                ler(connection, "historico_de_versionamento")
                submenu(connection, "hitorico_de_versionamento")
            case '6':
                ler(connection, "instituicao")
                submenu(connection, "instituicao")
            case '7':
                ler(connection, "plano")
                submenu(connection, "plano")
            case '8':
                ler(connection, "possui")
                submenu(connection, "possui")
            case '9':
                ler(connection, "usuario")
                submenu(connection, "usuario")
            case '0':
                break
            case _:
                print("Opção inválida.")

    connection.close()
    print("Saindo do programa...")

if __name__ == "__main__":
    main()