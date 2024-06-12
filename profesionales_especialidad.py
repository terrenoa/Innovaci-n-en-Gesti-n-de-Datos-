import mysql.connector
from mysql.connector import Error
conexion = mysql.connector.connect(
           host="localhost",
           port=3306,
           user="root",
           password="74269851vV",
           db="mydb" 
)

cursor = conexion.cursor()


def crear_prof_espe(Profesionales_idProfesionales, Especialidad_idEspecialidad):
    sql = "INSERT INTO profesionales_has_especialidad (Profesionales_idProfesionales, Especialidad_idEspecialidad) VALUES ('{}', '{}')".format(Profesionales_idProfesionales, Especialidad_idEspecialidad)
    values = ()
    cursor.execute(sql)
    conexion.commit()

def eliminar_prof_espe():
    id_prof = input("Ingrese el id del profesional a eliminar de la relacion: ")
    id_espe = input("Ingrese el id de la especialidad: ")
    sql = "DELETE FROM profesionales_has_especialidad WHERE Profesionales_idProfesionales=%s and Especialidad_idEspecialidad=%s"
    cursor.execute(sql,(id_prof, id_espe))
    conexion.commit()

def list_prof_espe():
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


def profesional_especialidad():
    print("\n")
    # Implementación de la función
    print("Profesionales-Especialidad")

    

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Relacion Profesional-Especialidad')
        print('2. Eliminar Relacion ')
        print('3. Listado')
        print('4. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
            print("\n")
            prof_in = input("Ingrese el id del profesional: ")
            espe_in = input("Ingrese el id de la especialidad: ")
            crear_prof_espe(prof_in, espe_in)


        elif option_pac == '2':
           print("\n")
           eliminar_prof_espe()
    

        elif option_pac == '3':
            print("\n")
            list_prof_espe()
            print("\n")
            
    
        elif option_pac == '4':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')

profesional_especialidad()