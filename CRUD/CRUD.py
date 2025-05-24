import mysql.connector
from mysql.connector import Error


# Conexão
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

        print(f"\nRegistros da tabela {tabela}:\n")
        print(" | ".join(colunas))  # Imprime cabeçalho com separador

        for linha in resultados:
            print(" | ".join(str(campo) for campo in linha))

    except Error as e:
        print(f"Erro ao ler tabela {tabela}:", e)

def atualizar(connection, nome_tabela):
    cursor = connection.cursor()

    # 1. Obter os nomes das colunas da tabela
    try:
        cursor.execute(f"SELECT * FROM {nome_tabela} LIMIT 0")
        nomes_colunas = [descricao[0] for descricao in cursor.description]
        cursor.fetchall()
    except Error as erro:
        print(f"Ocorreu um erro ao obter as colunas da tabela '{nome_tabela}': {erro}")
        return

    # 2. Perguntar qual ID será utilizado na atualização
    id_coluna = nomes_colunas[0]  # Assume que a primeira coluna é o ID
    id_valor = input(f"- Informe o valor de '{id_coluna}' do registro a ser atualizado: ").strip()
    if id_valor.isdigit():
        id_valor = int(id_valor)
    else:
        try:
            id_valor = float(id_valor)
        except ValueError:
            pass  # permanece como string

    # 3. Coletar qual coluna será atualizada e a nova informação
    nome_coluna = input("- Informe o nome da coluna que deseja atualizar: ").strip()
    if nome_coluna not in nomes_colunas:
        print(f"Coluna '{nome_coluna}' não existe na tabela '{nome_tabela}'.")
        return

    nova_info = input(f"- Informe o novo valor para a coluna '{nome_coluna}': ").strip()
    if nova_info.isdigit():
        nova_info = int(nova_info)
    else:
        try:
            nova_info = float(nova_info)
        except ValueError:
            pass  # permanece como string

    # 4. Executar o UPDATE no banco de dados
    sql_update = f"UPDATE {nome_tabela} SET {nome_coluna} = %s WHERE {id_coluna} = %s"

    try:
        cursor.execute(sql_update, (nova_info, id_valor))
        connection.commit()
        print(f"\nRegistro com {id_coluna} = {id_valor} atualizado com sucesso na tabela '{nome_tabela}'.")
    except Error as erro:
        print(f"Ocorreu um erro ao atualizar a tabela '{nome_tabela}': {erro}")

# 1
def excluir_admin(connection, id_admin):
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM admin WHERE id = %s", (id_admin,))
        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhum registro com ID {id_admin} foi encontrado na tabela 'admin'.")
        else:
            print(f"\nRegistro da tabela 'admin' com ID {id_admin} foi excluído com sucesso.")
    except Error as erro:
        print(f"Ocorreu um erro ao remover da tabela 'admin': {erro}")

# 2
def excluir_arquivo(connection, id_arquivo):
    cursor = connection.cursor()

    try:
        # 1. Excluir comentários relacionados
        cursor.execute("""
            DELETE FROM comentario WHERE id_arquivo = %s
        """, (id_arquivo,))

        # 2. Excluir compartilhamentos relacionados
        cursor.execute("""
            DELETE FROM compartilhamento WHERE id_arquivo = %s
        """, (id_arquivo,))

        # 3. Excluir registros de "possui"
        cursor.execute("""
            DELETE FROM possui WHERE id_arquivo = %s
        """, (id_arquivo,))

        # 4. Excluir histórico de versionamento
        cursor.execute("""
            DELETE FROM historico_de_versionamento WHERE id_arquivo = %s
        """, (id_arquivo,))

        # 5. Excluir o próprio arquivo
        cursor.execute("""
            DELETE FROM arquivo WHERE id = %s
        """, (id_arquivo,))

        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhum registro com ID {id_arquivo} foi encontrado na tabela 'arquivo'.")
        else:
            print(f"\nArquivo com ID {id_arquivo} e suas dependências foram excluídos com sucesso.")
    
    except Error as erro:
        print(f"Ocorreu um erro ao excluir o arquivo e suas dependências: {erro}")

# 3
def excluir_comentario(connection, id_comentario):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM comentario WHERE id = %s
        """, (id_comentario,))
        
        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhum comentário com ID {id_comentario} foi encontrado.")
        else:
            print(f"\nComentário com ID {id_comentario} foi excluído com sucesso.")
    
    except Error as erro:
        print(f"Ocorreu um erro ao excluir o comentário: {erro}")

# 4
def excluir_compartilhamento(connection, id_compartilhamento):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM compartilhamento WHERE id_compartilhamento = %s
        """, (id_compartilhamento,))
        
        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhum compartilhamento com ID {id_compartilhamento} foi encontrado.")
        else:
            print(f"\nCompartilhamento com ID {id_compartilhamento} foi excluído com sucesso.")
    
    except Error as erro:
        print(f"Ocorreu um erro ao excluir o compartilhamento: {erro}")

# 5
def excluir_historico_de_versionamento(connection, id_historico_de_versionamento):
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM historico_de_versionamento WHERE id_historico = %s
        """, (id_historico_de_versionamento,))
        
        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhum histórico com ID {id_historico_de_versionamento} foi encontrado.")
        else:
            print(f"\nHistórico com ID {id_historico_de_versionamento} foi excluído com sucesso.")
    
    except Error as erro:
        print(f"Ocorreu um erro ao excluir o histórico de versionamento: {erro}")

# 6
def excluir_instituicao(connection, id_instituicao):
    cursor = connection.cursor()

    try:
        # Excluir compartilhamentos envolvendo usuários da instituição
        cursor.execute("""
            DELETE FROM compartilhamento
            WHERE id_user_send IN (
                SELECT id FROM usuario WHERE id_instituicao = %s
            )
            OR id_user_receive IN (
                SELECT id FROM usuario WHERE id_instituicao = %s
            )
        """, (id_instituicao, id_instituicao))

        # Excluir comentários de usuários da instituição
        cursor.execute("""
            DELETE FROM comentario
            WHERE id_usuario IN (
                SELECT id FROM usuario WHERE id_instituicao = %s
            )
        """, (id_instituicao,))

        # Excluir histórico de versionamento de usuários da instituição
        cursor.execute("""
            DELETE FROM historico_de_versionamento
            WHERE id_usuario IN (
                SELECT id FROM usuario WHERE id_instituicao = %s
            )
        """, (id_instituicao,))

        # Excluir registros em 'possui' vinculados a usuários da instituição
        cursor.execute("""
            DELETE FROM possui
            WHERE id_usuario IN (
                SELECT id FROM usuario WHERE id_instituicao = %s
            )
        """, (id_instituicao,))

        # Excluir os próprios usuários
        cursor.execute("""
            DELETE FROM usuario
            WHERE id_instituicao = %s
        """, (id_instituicao,))

        # Excluir a própria instituição
        cursor.execute("""
            DELETE FROM instituicao
            WHERE id = %s
        """, (id_instituicao,))

        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhuma instituição com ID {id_instituicao} foi encontrada.")
        else:
            print(f"\nInstituição com ID {id_instituicao} e suas dependências foram excluídas com sucesso.")

    except Error as erro:
        print(f"Ocorreu um erro ao excluir a instituição: {erro}")

# 7
def excluir_plano(connection, id_plano):
    cursor = connection.cursor()

    # Passo 1: apagar dependências em ordem segura
    cursor.execute("""
        DELETE FROM compartilhamento 
        WHERE id_user_send IN (
            SELECT id FROM usuario WHERE id_instituicao IN (
                SELECT id FROM instituicao WHERE id_plano = %s
            )
        )
        OR id_user_receive IN (
            SELECT id FROM usuario WHERE id_instituicao IN (
                SELECT id FROM instituicao WHERE id_plano = %s
            )
        )
    """, (id_plano, id_plano))

    cursor.execute("""
        DELETE FROM comentario
        WHERE id_usuario IN (
            SELECT id FROM usuario WHERE id_instituicao IN (
                SELECT id FROM instituicao WHERE id_plano = %s
            )
        )
    """, (id_plano,))

    cursor.execute("""
        DELETE FROM historico_de_versionamento
        WHERE id_usuario IN (
            SELECT id FROM usuario WHERE id_instituicao IN (
                SELECT id FROM instituicao WHERE id_plano = %s
            )
        )
    """, (id_plano,))

    cursor.execute("""
        DELETE FROM possui
        WHERE id_usuario IN (
            SELECT id FROM usuario WHERE id_instituicao IN (
                SELECT id FROM instituicao WHERE id_plano = %s
            )
        )
    """, (id_plano,))

    cursor.execute("""
        DELETE FROM usuario
        WHERE id_instituicao IN (
            SELECT id FROM instituicao WHERE id_plano = %s
        )
    """, (id_plano,))

    cursor.execute("DELETE FROM instituicao WHERE id_plano = %s", (id_plano,))
    cursor.execute("DELETE FROM plano WHERE id = %s", (id_plano,))
    connection.commit()
    print(f"\nPlano com ID {id_plano} e suas dependências foram excluídos.")

# 8
def excluir_usuario(connection, id_usuario):
    cursor = connection.cursor()

    try:
        # Passo 1: apagar dependências em ordem segura
        cursor.execute("""
            DELETE FROM compartilhamento
            WHERE id_user_send = %s OR id_user_receive = %s
        """, (id_usuario, id_usuario))

        cursor.execute("""
            DELETE FROM comentario
            WHERE id_usuario = %s
        """, (id_usuario,))

        cursor.execute("""
            DELETE FROM historico_de_versionamento
            WHERE id_usuario = %s OR id_usuario_que_alterou = %s
        """, (id_usuario, id_usuario))

        cursor.execute("""
            DELETE FROM possui
            WHERE id_usuario = %s
        """, (id_usuario,))

        # Passo 2: remover o próprio usuário
        cursor.execute("""
            DELETE FROM usuario
            WHERE id = %s
        """, (id_usuario,))

        connection.commit()

        if cursor.rowcount == 0:
            print(f"\nNenhum usuário encontrado com ID {id_usuario}.")
        else:
            print(f"\nUsuário com ID {id_usuario} e suas dependências foram removidos com sucesso.")

    except Error as erro:
        print(f"Ocorreu um erro ao excluir o usuário {id_usuario}: {erro}")

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
                print(f"\n============= OPERACOES TABELA =============\n")
                print("Escolha a tabela para realizar remoção:")
                print("1 - Admin")
                print("2 - Arquivo")
                print("3 - Comentário")
                print("4 - Compartilhamento")
                print("5 - Histórico de versionameto")
                print("6 - Instituição")
                print("7 - Plano")
                print("8 - Usuários")
                print("0 - Sair")
                print("\n==============================================\n")
                table = input('Insira a tabela que voce deseja realizar a remoção: ')
                match table:
                    case '1':
                        ler(connection, "admin")
                        id_admin = input('\nInsira o ID da tabela admin que voce deseja remover: ')
                        excluir_admin(connection, id_admin)
                    case '2':
                        ler(connection, "arquivo")
                        id_arquivo = input('\nInsira o ID da tabela arquivo que voce deseja remover: ')
                        excluir_arquivo(connection, id_arquivo)
                    case '3':
                        ler(connection, "comentario")
                        id_comentario = input('\nInsira o ID da tabela comentario que voce deseja remover: ')
                        excluir_comentario(connection, id_comentario)
                    case '4':
                        ler(connection, "compartilhamento")
                        id_compartilhamento = input('\nInsira o ID da tabela compartilhamento que voce deseja remover: ')
                        excluir_compartilhamento(connection, id_compartilhamento)
                    case '5':
                        ler(connection, "historico_de_versionamento")
                        id_historico_de_versionamento = input('\nInsira o ID da tabela historico_de_versionamento que voce deseja remover: ')
                        excluir_historico_de_versionamento(connection, id_historico_de_versionamento)
                    case '6':
                        ler(connection, "instituicao")
                        id_instituicao = input('\nInsira o ID da tabela instituicao que voce deseja remover: ')
                        excluir_instituicao(connection, id_instituicao)
                    case '7':
                        ler(connection, "plano")
                        id_plano = input('\nInsira o ID da tabela plano que voce deseja remover: ')
                        excluir_plano(connection, id_plano)
                    case '8':
                        ler(connection, "usuario")
                        id_usuario = input('\nInsira o ID da tabela usuario que voce deseja remover: ')
                        excluir_usuario(connection, id_usuario)
                    case '0':
                        break
                    case _:
                        print('Opção inválida')
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
        print("5 - Histórico de versionamento")
        print("6 - Instituição")
        print("7 - Plano")
        print("8 - Usuários")
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
