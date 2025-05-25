class delete:
    def deletarUsuario(id):
        comando: f"""
            DELETE FROM usuario
            WHERE id = '{id}';
        """
        return comando
    
    def deletarAdmin():
        comando = f"""
            DELETE FROM Admin
            WHERE id = '{id}';
        """
        return comando

    def deletarArquivo():
        comando = f"""
            DELETE FROM arquivo
            WHERE id = '{id}'
        """
        return comando

    def deletarHistorico():
        comando = f"""
            DELETE FROM historico_de_versionamento
            WHERE id = '{id}';
        """
        return comando

    def deletarCompartilhamento():
        comando = f"""
            DELETE FROM compartilhamento
            WHERE id = '{id}';
        """
        return comando
    
    def deletarAtividadesRecentes():
        comando = f"""
            DELETE FROM atividades_recentes
            WHERE id = '{id}';
        """
        return comando
    
    def deletarPlano():
        comando = f"""
            DELETE FROM plano
            WHERE id = '{id}'
        """
        return comando
    
    def deletarInstituicao():
        comando = f"""
            DELETE FROM instituicao
            WHERE id = '{id}'
        """
        return comando

    def deletarPossui():
        comando = f"""
            DELETE FROM possui
            WHERE id = '{id}'
        """
        return comando