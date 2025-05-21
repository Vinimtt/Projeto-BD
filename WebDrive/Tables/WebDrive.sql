CREATE DATABASE WebDrive;
USE WebDrive;

CREATE TABLE plano (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    duracao VARCHAR(100),
    data_aquisicao VARCHAR(100),
    espaco_usuario DOUBLE
);

INSERT INTO plano (nome,duracao,data_aquisicao,espaco_usuario) VALUES
('Plano basico', '12', '27/02/2004', 30.0),
('Plano Medio', '24', '19/09/2003', 45.0),
('Plano Premium', '36', '27/08/2005', 60.0),
('Plano legado', '48', '28/01/2005', 75.0),
('Plano empresarial', '60', '28/05/2025', 100.0);

CREATE TABLE instituicao (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    causa_social VARCHAR(100),
    endereco VARCHAR(100),
    id_plano INT,
    FOREIGN KEY (id_plano) REFERENCES plano(id)
);

INSERT INTO instituicao (nome,causa_social,endereco,id_plano) VALUES
('Instituicao Alpha', 'Educacao', 'Rua A, 123', 1),
('Instituicao Beta', 'Saude', 'Rua B, 245', 2),
('Instituicao Sobrou Nada', 'Esportes', 'Rua C, 678',3),
('Centro Delta', 'Cultura', 'Av. D, 101', 4),
('ONG Epsilon', 'Meio Ambiente', 'Rua E, 202', 5);

CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(100),
    senha VARCHAR(100),
    email VARCHAR(100),
    data_ingresso VARCHAR(100),
    id_instituicao INT,
    FOREIGN KEY (id_instituicao) REFERENCES instituicao(id)
);

INSERT INTO usuario (login, senha, email, data_ingresso, id_instituicao) VALUES
('joaovictor', 'senha123', 'joao@email.com', '2024-01-20', 1),
('mariaclara', 'senha456', 'maria@email.com', '2024-01-25', 2),
('lucasribeiro', 'senha789', 'lucas@email.com', '2024-02-15', 3),
('anabeatriz', 'senha321', 'ana@email.com', '2024-03-01', 4),
('pedroalves', 'senha654', 'pedro@email.com', '2024-04-10', 5);

CREATE TABLE arquivo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_de_ultima_alteracao DATETIME,
    url VARCHAR(100),
    localizacao VARCHAR(100),
    permissao_de_acesso BOOLEAN,
    nome VARCHAR(100),
    tipo VARCHAR(100),
    tamanho VARCHAR(100)
);

INSERT INTO arquivo (data_de_ultima_alteracao, url, localizacao, permissao_de_acesso, nome, tipo, tamanho) VALUES
('2024-05-01 10:00:00', 'url.com/doc1', '/docs', TRUE, 'Relatório Anual', 'pdf', '2MB'),
('2024-05-02 12:00:00', 'url.com/img1', '/imagens', FALSE, 'Imagem Equipe', 'jpg', '1.5MB'),
('2024-05-03 14:00:00', 'url.com/ppt1', '/apresentacoes', TRUE, 'Apresentação Projeto', 'pptx', '3MB'),
('2024-05-04 09:30:00', 'url.com/plan1', '/planilhas', TRUE, 'Orçamento 2024', 'xlsx', '500KB'),
('2024-05-05 11:15:00', 'url.com/zip1', '/arquivos', FALSE, 'Backup', 'zip', '10MB');

CREATE TABLE compartilhamento (
    id_compartilhamento INT PRIMARY KEY AUTO_INCREMENT,
    data_compartilhamento VARCHAR(100),
    id_arquivo INT,
    id_user_send INT,
    id_user_receive INT,
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id),
    FOREIGN KEY (id_user_send) REFERENCES usuario(id),
    FOREIGN KEY (id_user_receive) REFERENCES usuario(id)
);

INSERT INTO compartilhamento (data_compartilhamento, id_arquivo, id_user_send, id_user_receive) VALUES
('2024-05-06', 1, 1, 2),
('2024-05-07', 2, 2, 3),
('2024-05-08', 3, 3, 4),
('2024-05-09', 4, 4, 5),
('2024-05-10', 5, 5, 1);

CREATE TABLE possui (
    id_usuario INT AUTO_INCREMENT,
    id_arquivo INT AUTO_INCREMENT,
    PRIMARY KEY (id_usuario, id_arquivo),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
);

INSERT INTO possui (id_usuario, id_arquivo) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

CREATE TABLE comentario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    conteudo VARCHAR(100),
    data DATE,
    hora TIME,
    id_usuario INT,
    id_arquivo INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
);

INSERT INTO comentario (conteudo, data, hora, id_usuario, id_arquivo) VALUES
('Bom arquivo!', '2024-05-06', '10:30:00', 2, 1),
('Precisa de revisão.', '2024-05-07', '11:00:00', 3, 2),
('Tudo certo.', '2024-05-08', '12:15:00', 4, 3),
('Faltam dados.', '2024-05-09', '09:45:00', 5, 4),
('Excelente.', '2024-05-10', '14:00:00', 1, 5);

CREATE TABLE historico_de_versionamento (
    id_historico INT PRIMARY KEY AUTO_INCREMENT,
    data DATE,
    hora TIME,
    operacao VARCHAR(100),
    id_usuario INT,
    id_usuario_que_alterou INT,
    conteudo_alterado VARCHAR(100),
    id_arquivo INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
);


INSERT INTO historico_de_versionamento (data, hora, operacao, id_usuario, id_usuario_que_alterou, conteudo_alterado, id_arquivo) VALUES
('2024-05-01', '10:15:00', 'upload', 1, 1, 'Upload inicial', 1),
('2024-05-02', '12:15:00', 'edição', 2, 2, 'Imagem redimensionada', 2),
('2024-05-03', '14:20:00', 'atualização', 3, 3, 'Título atualizado', 3),
('2024-05-04', '09:50:00', 'remoção', 4, 4, 'Removido gráfico', 4),
('2024-05-05', '11:30:00', 'upload', 5, 5, 'Backup enviado', 5);


CREATE TABLE Admin (
    id INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(100),
    senha VARCHAR(100),
    email VARCHAR(100),
    data_ingresso VARCHAR(100)
);

INSERT INTO Admin (login, senha, email, data_ingresso) VALUES
('admin1', 'admin123', 'admin1@webdrive.com', '2024-01-01'),
('admin2', 'admin456', 'admin2@webdrive.com', '2024-02-01'),
('admin3', 'admin789', 'admin3@webdrive.com', '2024-03-01'),
('admin4', 'admin321', 'admin4@webdrive.com', '2024-04-01'),
('admin5', 'admin654', 'admin5@webdrive.com', '2024-05-01');


