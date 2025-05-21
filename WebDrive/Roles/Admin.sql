CREATE USER IF NOT EXISTS 'PapelAdm'@'localhost' IDENTIFIED BY 'adm123';
GRANT SELECT, INSERT, UPDATE, DELETE ON WebDrive.* TO 'PapelAdm'@'localhost';

FLUSH privileges;