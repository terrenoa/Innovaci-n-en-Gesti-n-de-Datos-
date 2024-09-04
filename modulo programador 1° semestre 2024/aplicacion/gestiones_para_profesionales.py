# gestiones_para_profesionales.py es un archivo donde se gestionaran el ABM del profesionales
import mysql.connector
from mysql.connector import Error
from profesionales_especialidad import crear_prof_espe
from profesionales_especialidad import list_prof_espe
from profesionales_especialidad import eliminar_prof_espe
conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="74269851vV",
        db="mydb" 
    )

cursor = conexion.cursor()


def crear_profesionales(cuil, nombre, apellido): 
        sql = "INSERT INTO profesionales (cuil, nombre, apellido) VALUES ('{}','{}','{}')".format(cuil, nombre, apellido,) 
        values = ()
        cursor.execute(sql)
        conexion.commit()


def actualizar_profesional():
      cuil_in = input("Ingrese el cuil del profesional a modificar: ") 
      sql = "UPDATE profesionales SET nombre=%s, apellido=%s WHERE cuil=%s"
      nombre_act = input("Ingrese el nombre: ")
      apellido_act = input("Ingrese el apellido: ")
      cursor.execute(sql, (nombre_act, apellido_act, cuil_in,))
      conexion.commit()

def eliminar_profesionales():
        cuil_el = input("Ingrese el cuil del profesional a dar de baja: ")
        sql = "DELETE FROM profesionales WHERE cuil=%s"
        cursor.execute(sql,(cuil_el,))
        conexion.commit()

def listado_profesionales():
     cursor.execute("SELECT * from profesionales LIMIT 10")
     profesionales = cursor.fetchall()
     print("Listado de Profesionales:")
     for profesional in profesionales:
          print(profesional)

def gestiones_para_profesionales():
    # Implementación de la función
    print("Gestiones para profesionales")

    while True:
        print('\n')
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Profesional')
        print('2. Modificar Profesional')
        print('3. Baja Profesional')
        print('4. Listado de Profesionales')
        print('5. Asignar Especialidad')
        print('6. Eliminar Especialidad')
        print('7. Listado de Profesionales y Especialidades')
        print('8. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
             cuil_in = input("Ingrese el cuil del profesional: ")
             nombre_in = input("Ingrese el nombre: ")
             apellido_in = input("Ingrese el apellido: ")

             crear_profesionales(cuil_in, nombre_in, apellido_in)
            
### AGREGAR MENSAJE EXITOSO O FALLO


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

        
        elif option_pac == '6':
            eliminar_prof_espe()

        
        elif option_pac == '7':
            print("\n")
            list_prof_espe()


        elif option_pac == '8':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')


