# obras_sociales.py
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

def crear_especialidad(nombre):
     sql = "INSERT INTO especialidad (nombre) VALUES ('{}')".format(nombre)
     values = ()
     cursor.execute(sql)
     conexion.commit()

def actualizar_especialidad():
    id_in = input("Ingrese el id de la especialidad a modificar: ") 
    sql = "UPDATE especialidad SET nombre=%s WHERE idEspecialidad=%s"
    nombre_in = input("Ingrese el nombre: ")
    cursor.execute(sql, (nombre_in, id_in,))
    conexion.commit()

def eliminar_especialidad():
        id_in = input("Ingrese el id de la especialidad a eliminar: ")
        sql = "DELETE FROM especialidad WHERE idEspecialidad=%s"
        cursor.execute(sql,(id_in,))
        conexion.commit()

def listado_especialidad():
    cursor.execute("SELECT * from especialidad")
    especialidades = cursor.fetchall()
    print("Listado de especialidades:")
    for especialidad in especialidades:
        print(especialidad)



def especialidades():
    # Implementación de la función
    print("Especialidades")

    

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Especialidad')
        print('2. Modificar Especialidad')
        print('3. Eliminar Especialidad')
        print('4. Listado')
        print('5. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
             nombre_especialidad = input("Ingrese el nombre de la Especialidad: ")
             crear_especialidad(nombre_especialidad)


        elif option_pac == '2':
           actualizar_especialidad()
    

        elif option_pac == '3':
            eliminar_especialidad()
            
            
        elif option_pac == '4':
            print("\n")
            listado_especialidad()
            print("\n")

        elif option_pac == '5':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')
