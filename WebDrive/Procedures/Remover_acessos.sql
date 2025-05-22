DELIMITER $$

CREATE PROCEDURE Remover_acessos(IN id_arq INT)
BEGIN
    DELETE FROM compartilhamento WHERE id_arquivo = id_arq;
END $$

DELIMITER ;

CALL Remover_acessos(1);