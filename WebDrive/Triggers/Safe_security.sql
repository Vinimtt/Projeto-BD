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
