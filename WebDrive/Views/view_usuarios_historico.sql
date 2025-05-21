CREATE VIEW view_usuarios_historico AS
SELECT hv.operacao,hv.data,hv.hora,hv.conteudo_alterado

FROM historico_de_versionamento hv

WHERE hv.id_usuario = 1 --id_usuario_atual() alterar depois