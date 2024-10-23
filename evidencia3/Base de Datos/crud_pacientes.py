from conexionbd import conectar


def crear_paciente(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS): 
        cursor, conexion = conectar()
# Permite la inclusion de nuevos pacientes a la base de datos a paritr de la consulta INSERT
        sql = "INSERT INTO pacientes (dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) 
        # La consulta se almacena en la variable sql y a traves del cursor interactua con la bd
        values = ()
        cursor.execute(sql)
        #ejecuta la consulta
        conexion.commit()
        #guarda los cambios


def actualizar_paciente():
      cursor, conexion = conectar()
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
        cursor, conexion = conectar()
#Permite eliminar un registro de la bd a partir de la consulta DELETE
        dni_el = input("Ingrese el DNI del paciente a dar de baja: ") 
        #se utiliza como PK el dni para localizar el registro que se quiere modificar
        sql = "DELETE FROM pacientes WHERE dni=%s"
        cursor.execute(sql,(dni_el,))
        #ejecuta la consulta
        conexion.commit()
        #guarda los cambios


def listado_paciente():
     cursor, conexion = conectar()
#Esta consulta muestra un listado de toda la tabla
     cursor.execute("SELECT * from pacientes")
     pacientes = cursor.fetchall()
     print("Listado de Pacientes:")
     for paciente in pacientes:
          print(paciente)
        