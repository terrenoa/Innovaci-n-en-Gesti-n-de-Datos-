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

def crear_obras(nombre):
     sql = "INSERT INTO obras (nombre) VALUES ('{}')".format(nombre)
     values = ()
     cursor.execute(sql)
     conexion.commit()

def actualizar_obras():
    id_in = input("Ingrese el id de la Obra Social a modificar: ") 
    sql = "UPDATE obras SET nombre=%s WHERE idOS=%s"
    nombre_in = input("Ingrese el nombre: ")
    cursor.execute(sql, (nombre_in, id_in,))
    conexion.commit()

def eliminar_obras():
        id_in = input("Ingrese el id de la Obra Social a eliminar: ")
        sql = "DELETE FROM obras WHERE idOS=%s"
        cursor.execute(sql,(id_in,))
        conexion.commit()

def listado_obras():
    cursor.execute("SELECT * from obras")
    obras = cursor.fetchall()
    print("Listado de obras:")
    for obra in obras:
        print(obra)



def obras_sociales():
    # Implementación de la función
    print("Obras sociales")

    

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Obra Social')
        print('2. Modificar Obra Social')
        print('3. Eliminar Obra Social')
        print('4. Listado')
        print('5. Salir')
    
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
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')



