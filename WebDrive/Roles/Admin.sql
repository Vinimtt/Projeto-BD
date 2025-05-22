CREATE ROLE IF NOT EXISTS 'PapelAdm';

GRANT SELECT, INSERT, UPDATE, DELETE ON WebDrive.* TO 'PapelAdm';

CREATE USER IF NOT EXISTS 'administrador'@'localhost' IDENTIFIED BY 'adm123';

GRANT 'PapelAdm' TO 'administrador'@'localhost';

SET DEFAULT ROLE 'PapelAdm' TO 'administrador'@'localhost';

FLUSH PRIVILEGES;
