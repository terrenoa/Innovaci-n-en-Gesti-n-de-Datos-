from conexionbd import conectar

def crear_prof_espe(Profesionales_idProfesionales, Especialidad_idEspecialidad):
    cursor, conexion = conectar()
    sql = "INSERT INTO profesionales_has_especialidad (Profesionales_idProfesionales, Especialidad_idEspecialidad) VALUES ('{}', '{}')".format(Profesionales_idProfesionales, Especialidad_idEspecialidad)
    values = ()
    cursor.execute(sql)
    conexion.commit()

def eliminar_prof_espe():
    cursor, conexion = conectar()
    id_prof = input("Ingrese el id del profesional a eliminar de la relacion: ")
    id_espe = input("Ingrese el id de la especialidad: ")
    sql = "DELETE FROM profesionales_has_especialidad WHERE Profesionales_idProfesionales=%s and Especialidad_idEspecialidad=%s"
    cursor.execute(sql,(id_prof, id_espe))
    conexion.commit()

def list_prof_espe():
    cursor, conexion = conectar()
     # Consulta SQL para obtener los nombres de obras sociales y especialidades
    query = '''
    SELECT 
        profesionales.apellido AS profesionales_especialidad,
        profesionales.nombre AS profesionales_especialidad,
        especialidad.nombre AS nombre_especialidad
    FROM 
        profesionales
    JOIN 
        profesionales_has_especialidad ON profesionales.idProfesionales = profesionales_has_especialidad.Profesionales_idProfesionales
    JOIN 
        especialidad ON profesionales_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad
    '''
    cursor = conexion.cursor()  
    cursor.execute(query)  
    resultados = cursor.fetchall()  

    print( ("-"*25), "Especialidades por Profesional", ("-"*25))
    for resultado in resultados:
        print(f"Profesional: {resultado[0]}, {resultado[1]} // Especialidad: {resultado[2]}")
    
    print("-"*82)
    cursor.close()