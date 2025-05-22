DELIMITER $$

CREATE PROCEDURE Chavear(IN id_arq INT)
BEGIN
        IF(SELECT atividades_recentes.acesso FROM atividades_recentes WHERE id_arquivo = id_arq) = 'prioritário' THEN
            UPDATE atividades_recentes SET acesso = 'não prioritário' WHERE id_arquivo = id_arq;
        ELSE
            UPDATE atividades_recentes SET acesso = 'prioritário' WHERE id_arquivo = id_arq;
        END IF;
END $$;

DELIMITER;

CALL Chavear(1);
DROP PROCEDURE Chavear;