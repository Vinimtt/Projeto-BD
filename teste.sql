CREATE DATABASE WebDrive;
USE WebDrive;

CREATE TABLE plano (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    duracao VARCHAR(100),
    data_aquisicao VARCHAR(100),
    espaco_usuario DOUBLE
);

CREATE TABLE instituicao (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    causa_social VARCHAR(100),
    endereco VARCHAR(100),
    id_plano INT,
    FOREIGN KEY (id_plano) REFERENCES plano(id)
);

CREATE TABLE usuario (
    id INT PRIMARY KEY,
    login VARCHAR(100),
    senha VARCHAR(100),
    email VARCHAR(100),
    data_ingresso VARCHAR(100),
    id_instituicao INT,
    FOREIGN KEY (id_instituicao) REFERENCES instituicao(id)
);

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

CREATE TABLE compartilhamento (
    id_compartilhamento INT PRIMARY KEY,
    data_compartilhamento VARCHAR(100),
    id_arquivo INT,
    id_user_send INT,
    id_user_receive INT,
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id),
    FOREIGN KEY (id_user_send) REFERENCES usuario(id),
    FOREIGN KEY (id_user_receive) REFERENCES usuario(id)
);

CREATE TABLE possui (
    id_usuario INT,
    id_arquivo INT,
    PRIMARY KEY (id_usuario, id_arquivo),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
);

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

CREATE TABLE historico_de_versionamento (
    id_historico INT PRIMARY KEY,
    data DATE,
    hora TIME,
    operacao VARCHAR(100),
    id_usuario INT,
    id_usuario_que_alterou INT,
    conteudo_alterado VARCHAR(100),
    id_arquivo INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_usuario_que_alterou) REFERENCES usuario(id),
    FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
);

CREATE TABLE Admin (
    id INT PRIMARY KEY,
    login VARCHAR(100),
    senha VARCHAR(100),
    email VARCHAR(100),
    data_ingresso VARCHAR(100)
);
