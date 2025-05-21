import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="00000849115"  # Insira sua senha se estiver usando localmente
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
                id INT PRIMARY KEY,
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
                id INT PRIMARY KEY,
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
                data_de_ultima_alteracao DATETIME,
                url VARCHAR(100),
                localizacao VARCHAR(100),
                permissao_de_acesso BOOLEAN,
                nome VARCHAR(100),
                tipo VARCHAR(100),
                tamanho VARCHAR(100)
            )
            """,

            # Tabela compartilhamento
            """
            CREATE TABLE IF NOT EXISTS compartilhamento (
                id_compartilhamento INT PRIMARY KEY,
                data_compartilhamento VARCHAR(100),
                id_arquivo INT,
                id_user_send INT,
                id_user_receive INT,
                FOREIGN KEY (id_arquivo) REFERENCES arquivo(id),
                FOREIGN KEY (id_user_send) REFERENCES usuario(id),
                FOREIGN KEY (id_user_receive) REFERENCES usuario(id)
            )
            """,

            # Tabela possui
            """
            CREATE TABLE IF NOT EXISTS possui (
                id_usuario INT,
                id_arquivo INT,
                PRIMARY KEY (id_usuario, id_arquivo),
                FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
            )
            """,

            # Tabela comentario
            """
            CREATE TABLE IF NOT EXISTS comentario (
                id INT PRIMARY KEY AUTO_INCREMENT,
                conteudo VARCHAR(100),
                data DATE,
                hora TIME,
                id_usuario INT,
                id_arquivo INT,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
            )
            """,

            # Tabela historico_de_versionamento
            """
            CREATE TABLE IF NOT EXISTS historico_de_versionamento (
                id_historico INT PRIMARY KEY,
                data DATE,
                hora TIME,
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
                id INT PRIMARY KEY,
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

except Error as e:
    print("Erro ao executar:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
