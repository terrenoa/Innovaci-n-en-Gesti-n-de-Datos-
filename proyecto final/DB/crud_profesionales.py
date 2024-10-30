from .conexionbd import conectar
import mysql.connector
from mysql.connector import Error




def crear_profesionales(cuil, nombre, apellido): 
        cursor, conexion = conectar()
        sql = "INSERT INTO profesionales (cuil, nombre, apellido) VALUES ('{}','{}','{}')".format(cuil, nombre, apellido,) 
        values = ()
        cursor.execute(sql)
        conexion.commit()
        cursor.close()
        conexion.close()


def actualizar_profesional():
      cursor, conexion = conectar()
      cuil_in = input("Ingrese el cuil del profesional a modificar: ") 
      sql = "UPDATE profesionales SET nombre=%s, apellido=%s WHERE cuil=%s"
      nombre_act = input("Ingrese el nombre: ")
      apellido_act = input("Ingrese el apellido: ")
      cursor.execute(sql, (nombre_act, apellido_act, cuil_in,))
      conexion.commit()
      cursor.close()
      conexion.close()

def eliminar_profesionales():
        cursor, conexion = conectar()
        cuil_el = input("Ingrese el cuil del profesional a dar de baja: ")
        sql = "DELETE FROM profesionales WHERE cuil=%s"
        cursor.execute(sql,(cuil_el,))
        conexion.commit()
        cursor.close()
        conexion.close()

def listado_profesionales():
     cursor, conexion = conectar()
     cursor.execute("SELECT * from profesionales LIMIT 10")
     profesionales = cursor.fetchall()
     print("Listado de Profesionales:")
     for profesional in profesionales:
          print(profesional)
     cursor.close()
     conexion.close()

def gestiones_para_profesionales():
    
    # Implementación de la función
    print("\nGestiones para profesionales")

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Profesional')
        print('2. Modificar Profesional')
        print('3. Baja Profesional')
        print('4. Listado de Profesionales')
        print('5. Profesionales y sus Especialidades')
        print('6. Salir.')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
             cuil_in = input("Ingrese el cuil del profesional: ")
             nombre_in = input("Ingrese el nombre: ")
             apellido_in = input("Ingrese el apellido: ")

             crear_profesionales(cuil_in, nombre_in, apellido_in)

        elif option_pac == '2':
           actualizar_profesional()

        elif option_pac == '3':
            eliminar_profesionales()

        elif option_pac == '4':
            print("\n")
            listado_profesionales()
            print("\n")
        
        elif option_pac == '5':
             print("\n")
             profesionales_especialidades()
             print("\n")

        elif option_pac == '6':
            print('SESIÓN TERMINADA')
            break

        else:
            print('OPCIÓN INVÁLIDA')
            


#### PROFESIONALES-ESPECIALIDADES

def crear_prof_espe(Profesionales_idProfesionales, Especialidad_idEspecialidad):
    cursor, conexion = conectar()
    try:
            sql = "INSERT INTO profesionales_has_especialidad (Profesionales_idProfesionales, Especialidad_idEspecialidad) VALUES (%s, %s)"
            values = (Profesionales_idProfesionales, Especialidad_idEspecialidad)
            cursor.execute(sql, values)
            conexion.commit()
            print(f"\nEl profesional con ID {Profesionales_idProfesionales} ahora tiene la especialidad con ID {Especialidad_idEspecialidad}.")
    except mysql.connector.IntegrityError as e:
        #Si se pone algun ID invalido=====
        print("\nERROR, Verifica los ID ingresados.", e)
    finally:
            cursor.close()
            conexion.close()

def eliminar_prof_espe():
    cursor, conexion = conectar()
    id_prof = input("Ingrese el id del profesional a eliminar de la relacion: ")
    id_espe = input("Ingrese el id de la especialidad: ")
    try:
        sql = "DELETE FROM profesionales_has_especialidad WHERE Profesionales_idProfesionales=%s and Especialidad_idEspecialidad=%s"
        cursor.execute(sql,(id_prof, id_espe))
        conexion.commit()
    except mysql.connector.IntegrityError as e:
        print("\nERROR, Verifica los ID ingresados.", e)
    finally:
        cursor.close()
        conexion.close()
    
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
    
    cursor.execute(query)  
    resultados = cursor.fetchall()  

    print( ("-"*25), "Especialidades por Profesional", ("-"*25))
    for resultado in resultados:
        print(f"Profesional: {resultado[0]}, {resultado[1]} // Especialidad: {resultado[2]}")
    
    print("-"*82)
    cursor.close()
    conexion.close()

def profesionales_especialidades():
    cursor, conexion = conectar()
    while True:
        print("\nBienvenido al Menu de Gestion de Especialidades de Profesionales!")
        print("1. Agregar Especialidad a Profesional")
        print("2. Eliminar Especialidad de Profesional")
        print("3. Listado de Profesionales con sus respectivas especialidades")
        print('4. Salir')
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("\n")
            cursor.execute("SELECT * from profesionales")
            profesionales = cursor.fetchall()
            print("Listado ID de Profesionales:")
            for profesional in profesionales:
                print(profesional)
            
            cursor.execute("SELECT * from especialidad")
            especialidades = cursor.fetchall()
            print("Listado ID de especialidades:")
            for especialidad in especialidades:
                print(especialidad)
            
            prof_in = input("Ingrese el ID del profesional: ")
            espe_in = input("Ingrese el ID   de la especialidad: ")
            crear_prof_espe(prof_in, espe_in)

        elif opcion == "2":
            print("\n")
            eliminar_prof_espe()
            
        elif opcion == "3":
            list_prof_espe()

        elif opcion == "4":
            break
        
        else:
            print("\nOpcion invalida")
            break
        
