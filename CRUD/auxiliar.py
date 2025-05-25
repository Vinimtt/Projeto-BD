import mysql.connector
from mysql.connector import Error

def iniciar_banco():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
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
                )""",
                """CREATE TABLE IF NOT EXISTS atividades_recentes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    id_arquivo INT UNIQUE,
                    acesso VARCHAR(50),
                    ultima_versao DATETIME,
                    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
                ) ENGINE=InnoDB
            """

            ]
            
            print("Tabela atividades_recentes criada com sucesso!")

            for comando in tabelas:
                cursor.execute(comando)

            print("Todas as tabelas foram criadas com sucesso no banco WebDrive!")
            print("Tabela atividades_recentes criada com sucesso!")

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
            
            
        #Criação dos triggers    
        triggers = [
            """
            DELIMITER $$

            CREATE TRIGGER Registrar_operacao
            AFTER UPDATE ON arquivo
            FOR EACH ROW
            BEGIN
                UPDATE atividades_recentes
                    SET ultima_versao = NOW()
                    WHERE id_arquivo = NEW.id;
            END$$

            DELIMITER ;
            """
            
            """
            DELIMITER $$

            CREATE TRIGGER Safe_security
            BEFORE INSERT ON arquivo
            FOR EACH ROW
            BEGIN
                IF NEW.nome LIKE '%.exe' OR 
                NEW.nome LIKE '%.bat' OR 
                NEW.nome LIKE '%.sh' OR
                NEW.nome LIKE '%.msi' OR
                NEW.nome LIKE '%.cmd' THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = ' Arquivos executáveis não são permitidos.';
                END IF;
            END$$

            DELIMITER ;
            """
        ]    
            
        for trigger in triggers:
            cursor.execute(trigger)

        # CRIAÇÃO DAS PROCEDURES
        procedures = [

                """DROP PROCEDURE IF EXISTS Conta_usuarios""",
                """CREATE PROCEDURE Conta_usuarios(IN p_id_arq INT)
                BEGIN
                    DECLARE v_cont INT DEFAULT 0;
                    SELECT COUNT(DISTINCT u.id_usuario) INTO v_cont
                    FROM (
                        SELECT id_user_send AS id_usuario FROM compartilhamento WHERE id_arquivo = p_id_arq
                        UNION
                        SELECT id_user_receive AS id_usuario FROM compartilhamento WHERE id_arquivo = p_id_arq
                    ) AS u;
                    SELECT v_cont AS qtd_usuarios_com_acesso;
                END""",

                """DROP PROCEDURE IF EXISTS Chavear""",
                """CREATE PROCEDURE Chavear(IN p_id_arq INT)
                BEGIN
                    INSERT INTO atividades_recentes (id_arquivo, acesso, ultima_versao)
                    VALUES (p_id_arq, 'prioritário', NOW())
                    ON DUPLICATE KEY UPDATE
                        acesso = IF(acesso = 'prioritário', 'não prioritário', 'prioritário'),
                        ultima_versao = NOW();
                    SELECT CONCAT('Acesso do arquivo ', p_id_arq, ' alterado.') AS status_alteracao;
                END""",

                """DROP PROCEDURE IF EXISTS Verificar_atividades""",
                """CREATE PROCEDURE Verificar_atividades()
                BEGIN
                    UPDATE atividades_recentes
                    SET ultima_versao = NOW();
                    SELECT 'Ultima versão atualizada.' AS resultado;
                END""",

                """DROP PROCEDURE IF EXISTS Remover_acessos""",
                """CREATE PROCEDURE Remover_acessos(IN p_id_arq INT)
                BEGIN
                    DELETE FROM compartilhamento
                    WHERE id_arquivo = p_id_arq;
                    SELECT CONCAT('Acessos do arquivo ', p_id_arq, ' removidos.') AS resultado;
                END"""
            ]

        for proc in procedures:
                cursor.execute(proc)

        print("Procedures criadas com sucesso!")

    except Error as e:
        print("Erro ao executar:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão encerrada.")

def configurar_roles():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if connection.is_connected():
            print("Configurando roles e usuários...")
            cursor = connection.cursor()

            # PapelAdm
            cursor.execute("CREATE ROLE IF NOT EXISTS 'PapelAdm'")
            cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON WebDrive.* TO 'PapelAdm'")
            cursor.execute("CREATE USER IF NOT EXISTS 'administrador'@'localhost' IDENTIFIED BY 'adm123'")
            cursor.execute("GRANT 'PapelAdm' TO 'administrador'@'localhost'")
            cursor.execute("SET DEFAULT ROLE 'PapelAdm' TO 'administrador'@'localhost'")

            # PapelEmpresa
            cursor.execute("CREATE ROLE IF NOT EXISTS 'PapelEmpresa'")
            cursor.execute("GRANT SELECT ON WebDrive.usuario TO 'PapelEmpresa'")
            cursor.execute("GRANT SELECT ON WebDrive.arquivo TO 'PapelEmpresa'")
            cursor.execute("CREATE USER IF NOT EXISTS 'empresa'@'localhost' IDENTIFIED BY 'empresa123'")
            cursor.execute("GRANT 'PapelEmpresa' TO 'empresa'@'localhost'")
            cursor.execute("SET DEFAULT ROLE 'PapelEmpresa' TO 'empresa'@'localhost'")

            # falta terminar ainda
            cursor.execute("CREATE ROLE IF NOT EXISTS 'PapelUsuario'")
            cursor.execute("GRANT SELECT, INSERT, UPDATE ON WebDrive.arquivo TO 'PapelUsuario'")
            cursor.execute("CREATE USER IF NOT EXISTS 'usuario'@'localhost' IDENTIFIED BY 'usuario123'")
            cursor.execute("GRANT 'PapelUsuario' TO 'usuario'@'localhost'")
            cursor.execute("SET DEFAULT ROLE 'PapelUsuario' TO 'usuario'@'localhost'")

            cursor.execute("FLUSH PRIVILEGES")
            print("Roles e usuários configurados com sucesso!")

    except Error as e:
        print("Erro ao configurar roles:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão encerrada.")
