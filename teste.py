import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="WebDrive"
    )

    if connection.is_connected():
        print("Conectado com sucesso ao banco WebDrive.")
        cursor = connection.cursor()

        sql = """
        INSERT INTO plano (id, nome, duracao, data_aquisicao, espaco_usuario)
        VALUES (%s, %s, %s, %s, %s)
        """
        # Inserir o plano
        dados = (1, 'Plano basico', '12', '27/02/2004', 30.0)

        cursor.execute(sql, dados)
        connection.commit()

        print("Plano inserido com sucesso!")

except Error as e:
    print("Erro:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
