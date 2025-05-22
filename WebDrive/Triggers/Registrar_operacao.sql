DELIMITER $$

CREATE TRIGGER Registrar_operacao
AFTER UPDATE ON arquivo
FOR EACH ROW
BEGIN
    UPDATE atividades_recentes
    SET data_operacao = NOW()
    WHERE id_arquivo = NEW.id;
END$$

DELIMITER ;
