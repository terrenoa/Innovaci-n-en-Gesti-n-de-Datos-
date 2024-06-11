import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
           host="localhost",
           port=3306,
           user="root",
           password="74269851v",
           db="mydb" 
    )
    if conexion.is_connected():
         print("Conexión exitosa a la base de datos")
except Error as ex:
      print("Error durante la conexion.", ex)

cursor = conexion.cursor()


"""
sql = "insert into profesionales (cuil, nombre, apellido) values (%s, %s, %s)"
values = (20341, "jeronimo", "rodriguez")

cursor.execute(sql, values)

conexion.commit()


"""
dni_in = input("Ingrese el DNI: ")
nombre_in = input("Ingrese nombre: ")
apellido_in = input("ingrese el apellido: ")
telefono_in = input("Ingrese telefono: ")
direccion_in = input("Ingrese la direccion: ")
fecha_nacimiento_in = input("Ingrese la fecha de nacimiento: ")


# Crear un cursor
cursor = conexion.cursor()

    # Crear un nuevo paciente
def crear_paciente(dni, nombre, apellido, telefono, direccion, fecha_nacimiento): 
        sql = "INSERT INTO pacientes (dni, nombre, apellido, telefono, direccion, fecha_nacimiento) VALUES ('{}','{}','{}','{}','{}','{}')".format(dni, nombre, apellido, telefono, direccion, fecha_nacimiento) 
        values = ()
        cursor.execute(sql)
        conexion.commit()

crear_paciente(dni_in, nombre_in, apellido_in, telefono_in, direccion_in, fecha_nacimiento_in)

"""
    # Leer todos los pacientes
    def leer_pacientes():
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()
        return pacientes

    # Actualizar un paciente
    def actualizar_paciente(id_paciente, nombre, edad, enfermedad):
        sql = "UPDATE pacientes SET nombre='{}', edad={}, enfermedad='{}' WHERE id={}".format(nombre, edad, enfermedad, id_paciente)
        cursor.execute(sql)
        conexion.commit()

    # Eliminar un paciente
    def eliminar_paciente(id_paciente):
        sql = "DELETE FROM pacientes WHERE id={}".format(id_paciente)
        cursor.execute(sql)
        conexion.commit()

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