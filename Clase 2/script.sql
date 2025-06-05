-- Ejemplo de backup completo

CREATE SCHEMA IF NOT EXISTS ejemplo2;

USE ejemplo2;

CREATE TABLE USUARIO(
	id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(8) NOT NULL
);

INSERT INTO USUARIO(nombre, correo, telefono)
VALUES ('usuario 1', 'user1@example.com', '12345678'),
		('usuario 2', 'user2@example.com', '12345678'),
		('usuario 3', 'user3@example.com', '12345678'),
		('usuario 4', 'user4@example.com', '12345678');

-- Comando para crear un backup completo
-- mysqldump -u tu_usuario -p nombre_base_de_datos > nombre_archivo.sql