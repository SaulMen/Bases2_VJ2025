-- Modelo
CREATE SCHEMA IF NOT EXISTS ejemplo1;

USE ejemplo1;

-- Estudiante
CREATE TABLE ESTUDIANTE (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

-- Catedratico
CREATE TABLE CATEDRATICO (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

-- Curso 
CREATE TABLE CURSO (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion VARCHAR(100),
    cupo INTEGER
);

-- Asignacion/ inscripcion

CREATE TABLE INSCRIPCION (
    id INT PRIMARY KEY AUTO_INCREMENT,
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    fecha_inscripcion DATE NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTE(id),
    FOREIGN KEY (curso_id) REFERENCES CURSO(id)
);
