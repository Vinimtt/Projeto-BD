CREATE ROLE IF NOT EXISTS 'PapelEmpresa';

GRANT SELECT ON WebDrive.usuarios TO 'PapelEmpresa';
GRANT SELECT ON WebDrive.arquivos TO 'PapelEmpresa';

CREATE USER IF NOT EXISTS 'empresa'@'localhost' IDENTIFIED BY 'empresa123';

GRANT 'PapelEmpresa' TO 'empresa'@'localhost';

SET DEFAULT ROLE 'PapelEmpresa' TO 'empresa'@'localhost';

FLUSH PRIVILEGES;
