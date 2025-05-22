DELIMITER $$

CREATE TRIGGER Atualizar_acesso
AFTER INSERT ON possui
FOR EACH ROW
BEGIN
    UPDATE arquivo
    SET ultima_atualizacao = NOW()
    WHERE id = NEW.id_arquivo;
END$$

DELIMITER ;
