CREATE ROLE IF NOT EXISTS 'PapelUsuario';

GRANT SELECT, INSERT, UPDATE ON WebDrive.arquivo TO 'PapelUsuario';

CREATE USER IF NOT EXISTS 'usuario'@'localhost' IDENTIFIED BY 'usuario123';

GRANT 'PapelUsuario' TO 'usuario'@'localhost';

SET DEFAULT ROLE 'PapelUsuario' TO 'usuario'@'localhost';

FLUSH PRIVILEGES;

-- lembrar de adaptar para limitar aos proprios arquivos, acho que usa as views
