CREATE VIEW view_usuario AS
SELECT a.nome,a.tipo,a.tamanho,a.localizacao,a.url, a.data_de_ultima_alteracao

FROM arquivo a

WHERE a.id IN (

    SELECT id_arquivo FROM possui WHERE id_usuario = 1 --id_usuario_atual() atualizar depois 

    UNION
    
    SELECT id_arquivo FROM compartilhamento WHERE id_user_receive = 1 --id_usuario_atual() atualizar depois 
);