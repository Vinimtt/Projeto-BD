import mysql.connector
from mysql.connector import Error

# Parte 1: Conectar, criar banco e tabelas, e inserir registros de teste
def iniciar_banco():
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
            
            
            # 
            # 
            # 
            # 
            # 
            # 
            # 
            # 

            # TEsTE com procedure
            
            
            
            
            
            


def iniciar_banco_procedures():
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

            # Criação das tabelas
            tabelas = [
                """CREATE TABLE IF NOT EXISTS plano (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(100),
                    duracao VARCHAR(100),
                    data_aquisicao VARCHAR(100),
                    espaco_usuario DOUBLE
                )""",
                """CREATE TABLE IF NOT EXISTS instituicao (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(100),
                    causa_social VARCHAR(100),
                    endereco VARCHAR(100),
                    id_plano INT,
                    FOREIGN KEY (id_plano) REFERENCES plano(id)
                )""",
                """CREATE TABLE IF NOT EXISTS usuario (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    login VARCHAR(100),
                    senha VARCHAR(100),
                    email VARCHAR(100),
                    data_ingresso VARCHAR(100),
                    id_instituicao INT,
                    FOREIGN KEY (id_instituicao) REFERENCES instituicao(id)
                )""",
                """CREATE TABLE IF NOT EXISTS arquivo (
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
                )""",
                """CREATE TABLE IF NOT EXISTS compartilhamento (
                    id_compartilhamento INT PRIMARY KEY AUTO_INCREMENT,
                    data_compartilhamento VARCHAR(100),
                    id_arquivo INT,
                    id_user_send INT,
                    id_user_receive INT,
                    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id),
                    FOREIGN KEY (id_user_send) REFERENCES usuario(id),
                    FOREIGN KEY (id_user_receive) REFERENCES usuario(id)
                )""",
                """CREATE TABLE IF NOT EXISTS comentario (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    conteudo VARCHAR(100),
                    data VARCHAR(100),
                    hora VARCHAR(100),
                    id_usuario INT,
                    id_arquivo INT,
                    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
                )""",
                """CREATE TABLE IF NOT EXISTS historico_de_versionamento (
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
                )""",
                """CREATE TABLE IF NOT EXISTS Admin (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    login VARCHAR(100),
                    senha VARCHAR(100),
                    email VARCHAR(100),
                    data_ingresso VARCHAR(100)
                )"""
            ]

            for comando in tabelas:
                cursor.execute(comando)

            print("Todas as tabelas foram criadas com sucesso no banco WebDrive!")

            # CRIAÇÃO DAS PROCEDURES

            procedures = [
                """
                CREATE PROCEDURE Conta_usuarios(IN id_arq INT)
                BEGIN
                    DECLARE cont INT;
                    SELECT COUNT(DISTINCT id_user_send) INTO cont 
                    FROM WebDrive.compartilhamento 
                    WHERE id_arquivo = id_arq;

                    SET cont = cont + 1;

                    SELECT cont AS qtd_usuarios;
                END
                """,
                """
                CREATE PROCEDURE Chavear(IN id_arq INT)
                BEGIN
                    IF (SELECT acesso FROM atividades_recentes WHERE id_arquivo = id_arq LIMIT 1) = 'prioritário' THEN
                        UPDATE atividades_recentes 
                        SET acesso = 'não prioritário' 
                        WHERE id_arquivo = id_arq;
                    ELSE
                        UPDATE atividades_recentes 
                        SET acesso = 'prioritário' 
                        WHERE id_arquivo = id_arq;
                    END IF;
                END
                """,
                """
                CREATE PROCEDURE Verificar_atividades()
                BEGIN
                    UPDATE atividades_recentes 
                    SET ultima_versao = NOW();
                END
                """,
                """
                CREATE PROCEDURE Remover_acessos(IN id_arq INT)
                BEGIN
                    DELETE FROM compartilhamento 
                    WHERE id_arquivo = id_arq;
                END
                """
            ]

            for proc in procedures:
                cursor.execute(f"DROP PROCEDURE IF EXISTS {proc.split()[2]}")
                cursor.execute(f"DELIMITER $$")
                cursor.execute(proc)
                cursor.execute(f"DELIMITER ;")

            print("Procedures criadas com sucesso!")

            # Inserção de dados de teste
            cursor.execute("INSERT INTO plano (nome, duracao, data_aquisicao, espaco_usuario) VALUES ('Plano Básico', '12 meses', '2025-01-01', 10.0)")
            cursor.execute("INSERT INTO instituicao (nome, causa_social, endereco, id_plano) VALUES ('Instituto ABC', 'Educação', 'Rua X', 1)")
            cursor.execute("INSERT INTO usuario (login, senha, email, data_ingresso, id_instituicao) VALUES ('user1', '1234', 'user1@email.com', '2025-01-01', 1)")
            cursor.execute("INSERT INTO arquivo (data_de_ultima_alteracao, url, localizacao, permissao_de_acesso, nome, tipo, tamanho, id_usuario) VALUES ('2025-01-01', 'http://arquivo.com', 'pasta1', 'privado', 'arquivo1', 'txt', '1KB', 1)")
            cursor.execute("INSERT INTO compartilhamento (data_compartilhamento, id_arquivo, id_user_send, id_user_receive) VALUES ('2025-01-01', 1, 1, 1)")
            cursor.execute("INSERT INTO comentario (conteudo, data, hora, id_usuario, id_arquivo) VALUES ('Comentário teste', '2025-01-01', '10:00', 1, 1)")
            cursor.execute("INSERT INTO historico_de_versionamento (data, hora, operacao, id_usuario, id_usuario_que_alterou, conteudo_alterado, id_arquivo) VALUES ('2025-01-01', '10:00', 'Criação', 1, 1, 'Novo Conteúdo', 1)")
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


