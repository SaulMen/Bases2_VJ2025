-- Consultas

-- Ver estudiante por curso
USE ejemplo1;
SELECT c.id AS curso_id,
		c.nombre AS nombre_curso,
		c.cupo, COUNT(i.id) AS inscritos,
		(c.cupo - COUNT(i.id)) AS cupos_disponibles
FROM CURSO AS c
LEFT JOIN INSCRIPCION AS i ON c.id = i.curso_id
GROUP BY c.id, c.nombre, c.cupo;


-- ver los estudiantes inscritos a un curso específico
SELECT 
    e.nombre AS estudiante,
    c.nombre AS curso
FROM Inscripcion i
JOIN Estudiante e ON i.estudiante_id = e.id
JOIN CURSO c ON i.curso_id = c.id
WHERE c.nombre = 'IPC 2';

