DELIMITER$$
CREATE FUNCTION Verificar_data(id_arquivo INT)

RETURNS BOOLEAN
BEGIN 

        DECLARE data_comp DATE;
    SET data_comp :=(SELECT arquivo.data_ingresso FROM arquivo WHERE id = id_arquivo);
        IF DATEDIFF(data_de_ultima_alteracao(), data_comp) > 100 THEN
                RETURN TRUE;
    ELSE
                RETURN FALSE;
            END IF;
END$$

DELIMITER;
DROP FUNCTION Verificar_data;
