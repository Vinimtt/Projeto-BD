DELIMITER $$

CREATE PROCEDURE Verificar_atividades()
BEGIN
        UPDATE atividades_recentes SET ultima_versao = data_de_ultima_alteracao();
END $$

DELIMITER ;

CALL Verificar_atividades();
DROP PROCEDURE Verificar_atividades();