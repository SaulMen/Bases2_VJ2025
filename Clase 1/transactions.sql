-- TRANSACCION
DELIMITER $$
CREATE PROCEDURE AsignarCurso(
	IN Pestudiante_id INT,
    IN Pcurso_id INT
)

BEGIN
	DECLARE cupo_a INT;
    DECLARE inscritos_a INT;
    DECLARE cursos_totales INT;
    DECLARE ya_inscrito BOOLEAN DEFAULT FALSE;
    
    START TRANSACTION;

		SELECT cupo INTO cupo_a
        FROM CURSO
        WHERE id = Pcurso_id;
        
        -- Verificar si existe el curso
        IF cupo_a IS NULL THEN 
			ROLLBACK;
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se encontró el curso';
		END IF;
        
        --
        SELECT COUNT(*) INTO cursos_totales
        FROM INSCRIPCION
        WHERE Estudiante_id = Pestudiante_id;
        
        IF cursos_totales >= 3 THEN
			ROLLBACK;
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El estudiante excedió el limite de cursos a asignar';
        END IF;
        
        SELECT EXISTS(
			SELECT 1 FROM INSCRIPCION
            WHERE estudiante_id = Pestudiante_id AND curso_id = Pcurso_id
        ) INTO ya_inscrito;
        
        IF ya_inscrito THEN
			ROLLBACK;
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El estudiante ya está inscrito al curso';
		END IF;
        
        INSERT INTO Inscripcion (estudiante_id, curso_id, fecha_inscripcion)
        VALUES (Pestudiante_id, Pcurso_id, CURDATE());
        
        
        COMMIT; 
        
END$$

DELIMITER ;

SELECT * FROM INSCRIPCION;
SELECT * FROM ESTUDIANTE;
SELECT * FROM CURSO;

CALL AsignarCurso(5,4);