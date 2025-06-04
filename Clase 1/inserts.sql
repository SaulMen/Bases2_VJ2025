-- Inserts
INSERT INTO ESTUDIANTE (nombre, correo, fecha_nacimiento) 
VALUES ('Luis Pérez', 'luisp@gmail.com', '2002-05-18'),
('estudiante 1', 'es1@gmail.com', '2003-05-18'),
('estudiante 2', 'es2@gmail.com', '2004-05-18'),
('estudiante 3', 'es3@gmail.com', '2000-05-18'),
('estudiante 4', 'es4@gmail.com', '2001-05-18');

INSERT INTO CATEDRATICO(nombre)
VALUES ('ING. uno'),
('ING. dos'),
('ING. tres'),
('ING. cuatro');

INSERT INTO CURSO(nombre, descripcion, cupo)
VALUES ('IPC 1', 'Curso de IPC 1', 30),
('IPC 2', 'Curso de IPC 2', 30),
('OLC 1', 'Curso de OLC 1', 15),
('OLC 2', 'Curso de OLC 2', 15);

INSERT INTO INSCRIPCION(estudiante_id, curso_id, fecha_inscripcion)
VALUES (1, 1, '2025-06-03'),
(2, 1, '2025-06-04'),
(3, 2, '2025-06-03'),
(4, 2, '2025-06-05'),
(5, 3, '2025-06-06');
 



