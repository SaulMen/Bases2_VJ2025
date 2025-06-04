-- PROCEDURES
DELIMITER $$

CREATE PROCEDURE CrearEstudiante(
    IN p_nombre VARCHAR(100),
    IN p_correo VARCHAR(100),
    IN p_fecha_nacimiento DATE
)
BEGIN
    DECLARE edad INT;


    SET edad = TIMESTAMPDIFF(YEAR, p_fecha_nacimiento, CURDATE());


    IF edad > 75 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error: La edad no puede ser mayor a 75 años.';
    END IF;


    IF EXISTS (SELECT 1 FROM Estudiante WHERE correo = p_correo) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error: El correo ya está registrado.';
    END IF;


    INSERT INTO Estudiante (nombre, correo, fecha_nacimiento)
    VALUES (p_nombre, p_correo, p_fecha_nacimiento);
END$$

DELIMITER ;

CALL CrearEstudiante('Estudiante 6', 'ejemplo@gmail.com', '2000-04-12');

SELECT * FROM ESTUDIANTE;