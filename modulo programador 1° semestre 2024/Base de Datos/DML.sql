
-- nuevo paciente
INSERT INTO pacientes (dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) 
VALUES ('DNI', 'Nombre', 'Apellido', 'Telefono', 'Direccion', 'Fecha_Nacimiento', 'ObraS_idObraS');

-- actualizar paciente
UPDATE pacientes 
SET nombre = 'Nombre', apellido = 'Apellido', telefono = 'Telefono', direccion = 'Direccion', fecha_nacimiento = 'Fecha_Nacimiento', ObraS_idObraS = 'ObraS_idObraS'
WHERE dni = 'DNI';

-- baja paciente
DELETE FROM pacientes 
WHERE dni = 'DNI';

-- listado de todos los pacientes
SELECT * FROM pacientes;


-- nuevo profesional
INSERT INTO profesionales (cuil, nombre, apellido) 
VALUES ('CUIL', 'Nombre', 'Apellido');

-- actualizar datos de un profesional
UPDATE profesionales 
SET nombre = 'Nombre', apellido = 'Apellido' 
WHERE cuil = 'CUIL';

-- baja profesional
DELETE FROM profesionales 
WHERE cuil = 'CUIL';

-- lista de todos los profesionales
SELECT * FROM profesionales;


-- alta obra social
INSERT INTO obras (nombre) VALUES ('{}');

-- modificacion obra social
UPDATE obras 
SET nombre= 'nombre'
WHERE idOS= 'id';

-- baja obra social 
DELETE FROM obras WHERE idOS= 'id';

-- crear especialidad nueva 
INSERT INTO especialidad (nombre) VALUES ('{}');

-- actualizar especialidad 
UPDATE especialidad SET nombre='name' WHERE idEspecialidad='id';

-- baja especialidad 
DELETE FROM especialidad WHERE idEspecialidad='id';

-- listado especialidad

SELECT * from especialidad;


-- agregar especialidades a obra social
INSERT INTO obras_has_especialidad (ObraS_idOS, Especialidad_idEspecialidad) VALUES ('{}', '{}');

-- eliminar especialidad de una obra social

DELETE FROM obras_has_especialidad WHERE ObraS_idOS= 'id' and Especialidad_idEspecialidad='id';

-- listar las especialidades por obra social

SELECT 
        obras.nombre AS nombre_obra,
        especialidad.nombre AS nombre_especialidad
    FROM 
        obras
    JOIN 
        obras_has_especialidad ON obras.idOS = obras_has_especialidad.ObraS_idOS
    JOIN 
        especialidad ON obras_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad;
        
-- agregar una especialidad a un profesional
INSERT INTO profesionales_has_especialidad (Profesionales_idProfesionales, Especialidad_idEspecialidad) VALUES ('{}', '{}');

-- eliminar especialidad de un profesional
DELETE FROM profesionales_has_especialidad WHERE Profesionales_idProfesionales='id' and Especialidad_idEspecialidad='id';

-- listar especialidades por profesional
SELECT 
        profesionales.apellido AS profesionales_especialidad,
        profesionales.nombre AS profesionales_especialidad,
        especialidad.nombre AS nombre_especialidad
    FROM 
        profesionales
    JOIN 
        profesionales_has_especialidad ON profesionales.idProfesionales = profesionales_has_especialidad.Profesionales_idProfesionales
    JOIN 
        especialidad ON profesionales_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad;
        
-- mostrar especialidades para sacar un turno de un paciente por dni
SELECT especialidad.nombre,
    especialidad.idEspecialidad
    FROM pacientes
    JOIN obras ON pacientes.ObraS_idObraS = obras.idOS
    JOIN obras_has_especialidad ON obras.idOS = obras_has_especialidad.ObraS_idOS
    JOIN especialidad ON obras_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad
    WHERE pacientes.dni = 'dni';
 
 -- elegir especialidad para turno
 SELECT profesionales.nombre, profesionales.idProfesionales
    FROM profesionales_has_especialidad
    JOIN profesionales ON profesionales_has_especialidad.Profesionales_idProfesionales = profesionales.idProfesionales
    WHERE profesionales_has_especialidad.Especialidad_idEspecialidad = 'id';
    
-- cargar turno en la tabla
INSERT INTO turno (Pacientes_dni, Profesionales_idProfesionales, Especialidad_idEspecialidad, f_hora) VALUES ('dni', 'prof', 'especialidad', 'fecha y hora');

-- buscar turnos de una persona por dni
SELECT t.idTurno, t.Pacientes_dni, p.nombre AS Paciente, t.Profesionales_idProfesionales, 
           pr.apellido AS Profesional, t.Especialidad_idEspecialidad, e.nombre AS Especialidad,
           f_hora
    FROM turno t
    JOIN pacientes p ON t.Pacientes_dni = p.dni
    JOIN profesionales pr ON t.Profesionales_idProfesionales = pr.idProfesionales
    JOIN especialidad e ON t.Especialidad_idEspecialidad = e.idEspecialidad
    WHERE t.Pacientes_dni = 'dni';
    
-- listar todos los turnos
SELECT t.idTurno, t.Pacientes_dni, p.nombre AS Paciente, t.Profesionales_idProfesionales, 
           pr.apellido AS Profesional, t.Especialidad_idEspecialidad, e.nombre AS Especialidad,
           f_hora
    FROM turno t
    JOIN pacientes p ON t.Pacientes_dni = p.dni
    JOIN profesionales pr ON t.Profesionales_idProfesionales = pr.idProfesionales
    JOIN especialidad e ON t.Especialidad_idEspecialidad = e.idEspecialidad;










