-- Ejemplo de backup incremental

INSERT INTO USUARIO(nombre, correo, telefono)
VALUES ('usuario 5', 'user1@example.com', '12345678'),
		('usuario 6', 'user2@example.com', '12345678'),
		('usuario 7', 'user3@example.com', '12345678'),
		('usuario 8', 'user4@example.com', '12345678'),
		('usuario 9', 'user2@example.com', '12345678'),
		('usuario 10', 'user3@example.com', '12345678'),
		('usuario 11', 'user4@example.com', '12345678');
        
        