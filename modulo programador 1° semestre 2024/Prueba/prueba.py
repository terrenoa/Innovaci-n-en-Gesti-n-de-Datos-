import mysql.connector
from mysql.connector import Error
from gestiones_para_pacientes import gestiones_para_pacientes
try:
    conexion = mysql.connector.connect(
           host="localhost",
           port=3306,
           user="root",
           password="74269851vV",
           db="mydb" 
    )
    if conexion.is_connected():
         print("Conexión exitosa a la base de datos")
except Error as ex:
      print("Error durante la conexion.", ex)

cursor = conexion.cursor()











"""



dni_in = input("Ingrese el DNI: ")
nombre_in = input("Ingrese nombre: ")
apellido_in = input("ingrese el apellido: ")
telefono_in = input("Ingrese telefono: ")
direccion_in = input("Ingrese la direccion: ")
fecha_nacimiento_in = input("Ingrese la fecha de nacimiento: ")
ObraS_idObraS_in = input("Ingresear el id de la obra social: ")




# Crear un cursor
cursor = conexion.cursor()

    # Crear un nuevo paciente
def crear_paciente(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS): 
        sql = "INSERT INTO pacientes (dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(dni, nombre, apellido, telefono, direccion, fecha_nacimiento, ObraS_idObraS) 
        values = ()
        cursor.execute(sql)
        conexion.commit()

crear_paciente(dni_in, nombre_in, apellido_in, telefono_in, direccion_in, fecha_nacimiento_in, ObraS_idObraS_in)
"""

"""
    # Leer todos los pacientes
    def leer_pacientes():
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()
        return pacientes

    # Actualizar un paciente




def actualizar_paciente():
      dni_in = input("Ingrese el dni del paciente a modificar: ") 
      sql = "UPDATE pacientes SET nombre=%s, apellido=%s, telefono=%s, direccion=%s, fecha_nacimiento=%s, ObraS_idObras=%s WHERE dni=%s"
      nombre_act = input("Ingrese el nombre: ")
      apellido_act = input("Ingrese el apellido: ")
      telefono_act = input("Ingrese el numero telefonico: ")
      direccion_act = input("Ingrese la direccion: ")
      fecha_nacimiento_act = input("Ingrese la fecha de nacimiento: ")
      ObraS_idObras_act = input("Ingrese el id de la obra social: ")
      cursor.execute(sql, (nombre_act, apellido_act, telefono_act, direccion_act, fecha_nacimiento_act, ObraS_idObras_act, dni_in))
      conexion.commit()

actualizar_paciente()

"""

"""

def eliminar_paciente():
        dni_el = input("Ingrese el DNI del paciente a dar de baja: ")
        sql = "DELETE FROM pacientes WHERE dni=%s"
        cursor.execute(sql,(dni_el,))
        conexion.commit()

eliminar_paciente()
"""

"""
    # Ejemplo de uso
    # Crear un nuevo paciente
    crear_paciente("Juan", 30, "Gripe")

    # Leer todos los pacientes
    pacientes = leer_pacientes()
    print("Lista de pacientes:")
    for paciente in pacientes:
        print(paciente)

    # Actualizar un paciente
    actualizar_paciente(1, "Juan Pérez", 35, "Resfriado")

    # Eliminar un paciente
    eliminar_paciente(1)

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()

"""
"""
cursor.execute("SELECT * from pacientes")

pacientes = cursor.fetchall()
print("Listado de Pacientes:")
for paciente in pacientes:
     print(paciente)


cuil_in = input("Ingrese el cuil del profesional: ")
nombre_in = input("Ingrese el nombre: ")
apellido_in = input("Ingrese el apellido: ")

def crear_profesionales(cuil, nombre, apellido): 
        sql = "INSERT INTO profesionales (cuil, nombre, apellido) VALUES ('{}','{}','{}')".format(cuil, nombre, apellido,) 
        values = ()
        cursor.execute(sql)
        conexion.commit()

crear_profesionales(cuil_in, nombre_in, apellido_in)

"""
"""

def actualizar_profesional():
      cuil_in = input("Ingrese el cuil del profesional a modificar: ") 
      sql = "UPDATE profesionales SET nombre=%s, apellido=%s WHERE cuil=%s"
      nombre_act = input("Ingrese el nombre: ")
      apellido_act = input("Ingrese el apellido: ")
      cursor.execute(sql, (nombre_act, apellido_act, cuil_in,))
      conexion.commit()

actualizar_profesional()

"""
"""
def listado_profesionales():
     cursor.execute("SELECT * from profesionales")
     profesionales = cursor.fetchall()
     print("Listado de Profesionales:")
     for profesional in profesionales:
          print(profesional)
listado_profesionales()
"""
"""
def eliminar_profesionales():
        cuil_el = input("Ingrese el cuil del profesional a dar de baja: ")
        sql = "DELETE FROM profesionales WHERE cuil=%s"
        cursor.execute(sql,(cuil_el,))
        conexion.commit()
eliminar_profesionales()

"""
"""
cuil_in = input("Ingrese el cuil del profesional: ")
nombre_in = input("Ingrese el nombre: ")
apellido_in = input("Ingrese el apellido: ")

def crear_profesionales(cuil, nombre, apellido): 
        sql = "INSERT INTO profesionales (cuil, nombre, apellido) VALUES ('{}','{}','{}')".format(cuil, nombre, apellido,) 
        values = ()
        cursor.execute(sql)
        conexion.commit()

crear_profesionales(cuil_in, nombre_in, apellido_in)
"""
"""
nombreO_in = input("Ingresar el nombre de la Obra Social: ")
def crear_obras(nombre):
     sql = "INSERT INTO obras (nombre) VALUES('{}')".format(nombre,)
     values = ()
     cursor.execute(sql)
     conexion.commit()

crear_obras(nombreO_in)

"""
"""
def actualizar_obras():
    id_in = input("Ingrese el id de la Obra Social a modificar: ") 
    sql = "UPDATE obras SET nombre=%s WHERE idOS=%s"
    nombre_in = input("Ingrese el nombre: ")
    cursor.execute(sql, (nombre_in, id_in,))
    conexion.commit()

actualizar_obras()

"""
"""
def eliminar_obras():
        id_in = input("Ingrese el id de la Obra Social a eliminar: ")
        sql = "DELETE FROM obras WHERE idOS=%s"
        cursor.execute(sql,(id_in,))
        conexion.commit()

eliminar_obras()
"""
"""
def listado_obras():
    cursor.execute("SELECT * from obras")
    obras = cursor.fetchall()
    print("Listado de obras:")
    for obra in obras:
        print(obra)

listado_obras()
"""


gestiones_para_pacientes()