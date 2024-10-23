from conexionbd import conectar

def crear_obras(nombre):
     cursor, conexion = conectar()
     sql = "INSERT INTO obras (nombre) VALUES ('{}')".format(nombre)
     values = ()
     cursor.execute(sql)
     conexion.commit()

def actualizar_obras():
    cursor, conexion = conectar()
    id_in = input("Ingrese el id de la Obra Social a modificar: ") 
    sql = "UPDATE obras SET nombre=%s WHERE idOS=%s"
    nombre_in = input("Ingrese el nombre: ")
    cursor.execute(sql, (nombre_in, id_in,))
    conexion.commit()

def eliminar_obras():
        cursor, conexion = conectar()
        id_in = input("Ingrese el id de la Obra Social a eliminar: ")
        sql = "DELETE FROM obras WHERE idOS=%s"
        cursor.execute(sql,(id_in,))
        conexion.commit()

def listado_obras():
    cursor, conexion = conectar()
    cursor.execute("SELECT * from obras")
    obras = cursor.fetchall()
    print("Listado de obras:")
    for obra in obras:
        print(obra)