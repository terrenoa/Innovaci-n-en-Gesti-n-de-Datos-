# Archivo gestiones_para_pacientes.py es un archivo donde se gestionaran el ABM del paciente.
#se importan las librerias necesarias para poder conectar la aplicación con la base de datos

import mysql.connector
from mysql.connector import Error



def crear_paciente(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS): 
# Permite la inclusion de nuevos pacientes a la base de datos a paritr de la consulta INSERT
        sql = "INSERT INTO pacientes (dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) 
        # La consulta se almacena en la variable sql y a traves del cursor interactua con la bd
        values = ()
        cursor.execute(sql)
        #ejecuta la consulta
        conexion.commit()
        #guarda los cambios



def actualizar_paciente():
#Permite la edicion de un registro en la tabla de pacientes a partir de la consulta UPDATE
#Almacena los nuevos valores de las columnas en variables referenciales y con el cursor se insteran en la bd
      dni_in = input("Ingrese el dni del paciente a modificar: ")
      #se utiliza como PK el dni para localizar el registro que se quiere modificar
      sql = "UPDATE pacientes SET nombre=%s, apellido=%s, telefono=%s, direccion=%s, fecha_nacimiento=%s, ObraS_idObras=%s WHERE dni=%s"
      nombre_act = input("Ingrese el nombre: ")
      apellido_act = input("Ingrese el apellido: ")
      telefono_act = input("Ingrese el numero telefonico: ")
      direccion_act = input("Ingrese la direccion: ")
      fecha_nacimiento_act = input("Ingrese la fecha de nacimiento: ")
      ObraS_idObras_act = input("Ingrese el id de la obra social: ")
      cursor.execute(sql, (nombre_act, apellido_act, telefono_act, direccion_act, fecha_nacimiento_act, ObraS_idObras_act, dni_in))
      #ejecuta la consulta
      conexion.commit()
      #guarda los cambios
      #La información vieja se pierde



def eliminar_paciente():
#Permite eliminar un registro de la bd a partir de la consulta DELETE
        dni_el = input("Ingrese el DNI del paciente a dar de baja: ") 
        #se utiliza como PK el dni para localizar el registro que se quiere modificar
        sql = "DELETE FROM pacientes WHERE dni=%s"
        cursor.execute(sql,(dni_el,))
        #ejecuta la consulta
        conexion.commit()
        #guarda los cambios


def listado_paciente():
#Esta consulta muestra un listado de toda la tabla
     cursor.execute("SELECT * from pacientes")
     pacientes = cursor.fetchall()
     print("Listado de Pacientes:")
     for paciente in pacientes:
          print(paciente)


def gestiones_para_pacientes():
#Funcion principal del archivo
#Aplica todas las funciones definidas arriba
#se implementa en el archivo index.py
    print("Gestiones para pacientes")

    while True:
    #menu de opciones, cada funcion se relaciona con una opcion
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Paciente')
        print('2. Modificar Paciente')
        print('3. Baja Paciente')
        print('4. Listado')
        print('5. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
             dni_in = input("Ingrese el DNI: ")
             nombre_in = input("Ingrese nombre: ")
             apellido_in = input("ingrese el apellido: ")
             telefono_in = input("Ingrese telefono: ")
             direccion_in = input("Ingrese la direccion: ")
             fecha_nacimiento_in = input("Ingrese la fecha de nacimiento: ")
             ObraS_idObraS_in = input("Ingresear el id de la obra social: ")
             crear_paciente(dni_in, nombre_in, apellido_in, telefono_in, direccion_in, fecha_nacimiento_in, ObraS_idObraS_in)
            
### AGREGAR MENSAJE EXITOSO O FALLO


        elif option_pac == '2':
           actualizar_paciente()
    

        elif option_pac == '3':
            eliminar_paciente()

        elif option_pac == '4':
            print("\n")
            listado_paciente()
            print("\n")
        elif option_pac == '5':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')


