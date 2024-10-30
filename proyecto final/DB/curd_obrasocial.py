from .conexionbd import conectar
import mysql.connector
from mysql.connector import Error


def crear_obras(nombre):
     cursor, conexion = conectar()
     sql = "INSERT INTO obras (nombre) VALUES ('{}')".format(nombre)
     values = ()
     cursor.execute(sql)
     conexion.commit()
     cursor.close()
     conexion.close()

def actualizar_obras():
    cursor, conexion = conectar()
    id_in = input("Ingrese el id de la Obra Social a modificar: ") 
    sql = "UPDATE obras SET nombre=%s WHERE idOS=%s"
    nombre_in = input("Ingrese el nombre: ")
    cursor.execute(sql, (nombre_in, id_in,))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_obras():
        cursor, conexion = conectar()
        id_in = input("Ingrese el id de la Obra Social a eliminar: ")
        sql = "DELETE FROM obras WHERE idOS=%s"
        cursor.execute(sql,(id_in,))
        conexion.commit()
        cursor.close()
        conexion.close()

def listado_obras():
    cursor, conexion = conectar()
    cursor.execute("SELECT * from obras")
    obras = cursor.fetchall()
    print("Listado de obras:")
    for obra in obras:
        print(obra)
    cursor.close()
    conexion.close()





############# ESPECIALIDAD-OBRAS ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓




def crear_obras_espe(ObraS_idOS, Especialidad_idEspecialidad):
    cursor, conexion = conectar()
    sql = "INSERT INTO obras_has_especialidad (ObraS_idOS, Especialidad_idEspecialidad) VALUES ('{}', '{}')".format(ObraS_idOS, Especialidad_idEspecialidad)
    values = ()
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_obras_espe():
    cursor, conexion = conectar()
    id_obras = input("Ingrese el id de la obra a eliminar de la relacion: ")
    id_espe = input("Ingrese el id de la especialidad: ")
    sql = "DELETE FROM obras_has_especialidad WHERE ObraS_idOS=%s and Especialidad_idEspecialidad=%s"
    cursor.execute(sql,(id_obras, id_espe))
    conexion.commit()
    cursor.close()
    conexion.close()

def list_obras_espe():
    cursor, conexion = conectar()
    # Consulta SQL para obtener los nombres de obras sociales y especialidades
    query = """
    SELECT 
        obras.nombre AS nombre_obra,
        especialidad.nombre AS nombre_especialidad
    FROM 
        obras
    JOIN 
        obras_has_especialidad ON obras.idOS = obras_has_especialidad.ObraS_idOS
    JOIN 
        especialidad ON obras_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad
    """

    cursor = conexion.cursor()  
    cursor.execute(query)  
    resultados = cursor.fetchall()  

    print( ("-"*25), "Especialidades por Obra Social", ("-"*25))
    for resultado in resultados:
        print(f"Obra Social: {resultado[0]}, Especialidad: {resultado[1]}")
    
    print("-"*82)
    
    cursor.close()
    conexion.close()

def obras_especialidad():
    cursor, conexion = conectar()
    print("\n")
    print("Obras-Especialidad")


    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Asignar Especialidad cubierta por Obra Social')
        print('2. Eliminar Especialidad de Obra Social ')
        print('3. Listado De las Especialidades que cubre cada obra social')
        print('4. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
            cursor.execute("SELECT * from obras")
            obras = cursor.fetchall()
            print("Listado de obras:")
            for obra in obras:
                print(obra)
            cursor.execute("SELECT * from especialidad")
            especialidades = cursor.fetchall()
            print("Listado de especialidades:")
            for especialidad in especialidades:
                print(especialidad)

        elif option_pac == '2':
            eliminar_obras_espe()

        elif option_pac == '3':
            print("\n")
            list_obras_espe()
            print("\n")
            
    
        elif option_pac == '4':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')

def obras_sociales():
    # Implementación de la función
    print("Obras sociales")

    

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Obra Social')
        print('2. Modificar Obra Social')
        print('3. Eliminar Obra Social')
        print('4. Listado de Obras Sociales')
        print("5. Obras Sociales y Especialidades")
        print('8. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
             nombreO_in = input("Ingrese el nombre de la Obra Social: ")
             crear_obras(nombreO_in)


        elif option_pac == '2':
           actualizar_obras()
    

        elif option_pac == '3':
            eliminar_obras()
            
            
        elif option_pac == '4':
            print("\n")
            listado_obras()
            print("\n")
        
        elif option_pac == '5':
            obras_especialidad()

        elif option_pac == '8':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')
       
