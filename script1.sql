-- Ejemplo de backup completo

CREATE SCHEMA IF NOT EXISTS ejemplo3;

USE ejemplo3;

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
        
        
        
        
        
        
        
        
        
-- 'C:/ProgramData/MySQL/MySQL Server 8.0/Data/SAUL-bin.000188' 
-- SAUL-bin.000186
-- 7583426
