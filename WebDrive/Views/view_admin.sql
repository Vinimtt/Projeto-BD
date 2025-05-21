CREATE VIEW view_admin AS

SELECT a.nome,a.tipo,a.tamanho,a.localizacao, a.url, a.data_de_ultima_alteracao

FROM arquivo a;