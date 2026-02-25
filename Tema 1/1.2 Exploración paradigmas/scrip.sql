

SELECT 'Hola, este es un ejemplo del paradigma declarativo' AS mensaje;

SELECT 
    UPPER('programación declarativa') AS mayusculas,
    LENGTH('paradigma') AS longitud,
    CURRENT_DATE AS fecha_actual,
    ROUND(3.14159, 2) AS pi_redondeado;
    
SELECT 
nombre,
edad,
CASE 
        WHEN edad < 18 THEN 'Menor de edad'
        WHEN edad BETWEEN 18 AND 65 THEN 'Adulto'
        ELSE 'Adulto mayor'
    END AS categoria
FROM personas;

SELECT 
    CONCAT('El estudiante ', nombre, ' tiene ', edad, ' años') AS descripcion,
    CONCAT('Promedio: ', ROUND(promedio, 2), ' puntos') AS calificacion
FROM estudiantes
WHERE edad > 18;


CREATE TABLE tareas (
    id INT,
    nombre VARCHAR(50),
    prioridad VARCHAR(10),
    completada BOOLEAN
);

INSERT INTO tareas VALUES 
    (1, 'Estudiar', 'alta', false),
    (2, 'Hacer ejercicio', 'media', true),
    (3, 'Comprar comida', 'alta', false);

SELECT nombre 
FROM tareas
WHERE prioridad = 'alta' AND completada = false;






create database pruebas;
use pruebas;

CREATE TABLE personas (
Id int auto_increment not null primary key ,
nombre varchar(12),
edad int 
);

CREATE TABLE estudiantes (
Id int auto_increment not null primary key ,
nombre varchar(12),
edad int,
promedio float
);