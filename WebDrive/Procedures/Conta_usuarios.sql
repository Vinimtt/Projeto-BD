CREATE PROCEDURE Conta_usuarios(IN id_arq INT)
BEGIN
        DECLARE cont INT;
    SELECT COUNT(DISTINCT id_user_send) INTO cont FROM WebDrive.compartilhamento WHERE id_arquivo = id_arq;
    SET cont := cont+1;
    SELECT cont AS qtd_usuarios;
END $$

DELIMITER ;

CALL Conta_usuarios(1);
DROP PROCEDURE Conta_usuarios;
