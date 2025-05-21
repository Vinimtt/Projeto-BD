--tabela atividades_recentes ainda nao criada para o procedure Verificar_atividades

CREATE PROCEDURE Conta_usuarios(IN id_arq INT)
BEGIN
        DECLARE cont INT;
    SELECT COUNT(DISTINCT id_user_send) INTO cont FROM WebDrive.compartilhamento WHERE id_arquivo = id_arq;
    SET cont := cont+1;
    SELECT cont AS qtd_usuarios;
END $$

DELIMITER ;

CALL Conta_usuarios();
DROP PROCEDURE Conta_usuarios;

--tabela atividades_recentes ainda nao criada para o procedure Chavear

DELIMITER $$

CREATE PROCEDURE Remover_acessos(IN id_arq INT)
BEGIN
    DELETE FROM compartilhamento WHERE id_arquivo = id_arq;
END $$

DELIMITER ;

CALL Remover_acessos();