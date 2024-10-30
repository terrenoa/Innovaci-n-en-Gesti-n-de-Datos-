from .conexionbd import conectar


def crear_paciente(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS): 
        cursor, conexion = conectar()
#Permite meter nuevos pacientes a la base de datos a paritr de la consulta INSERT
        sql = "INSERT INTO pacientes (dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) 
        values = ()
        cursor.execute(sql)
        conexion.commit()
        cursor.close()
        conexion.close()


def actualizar_paciente():
      cursor, conexion = conectar()
#Permite la edicion de un registro en la tabla de pacientes a partir de la consulta UPDATE
#Almacena los nuevos valores de las columnas en variables referenciales y con el cursor se insteran en la db
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
      conexion.commit()
      cursor.close()
      conexion.close()


def eliminar_paciente():
        cursor, conexion = conectar()
        dni_el = input("Ingrese el DNI del paciente a dar de baja: ") 
        sql = "DELETE FROM pacientes WHERE dni=%s"
        cursor.execute(sql,(dni_el,))
        conexion.commit()
        cursor.close()
        conexion.close()
    

def listado_paciente():
     cursor, conexion = conectar()
     cursor.execute("SELECT * from pacientes")
     pacientes = cursor.fetchall()
     
     print("Listado de Pacientes:")
     for paciente in pacientes:
          print(paciente)
     cursor.close()
     conexion.close()

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
        
