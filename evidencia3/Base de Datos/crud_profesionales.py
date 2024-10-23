from conexionbd import conectar

def crear_profesionales(cuil, nombre, apellido): 
        cursor, conexion = conectar()
        sql = "INSERT INTO profesionales (cuil, nombre, apellido) VALUES ('{}','{}','{}')".format(cuil, nombre, apellido,) 
        values = ()
        cursor.execute(sql)
        conexion.commit()


def actualizar_profesional():
      cursor, conexion = conectar()
      cuil_in = input("Ingrese el cuil del profesional a modificar: ") 
      sql = "UPDATE profesionales SET nombre=%s, apellido=%s WHERE cuil=%s"
      nombre_act = input("Ingrese el nombre: ")
      apellido_act = input("Ingrese el apellido: ")
      cursor.execute(sql, (nombre_act, apellido_act, cuil_in,))
      conexion.commit()

def eliminar_profesionales():
        cursor, conexion = conectar()
        cuil_el = input("Ingrese el cuil del profesional a dar de baja: ")
        sql = "DELETE FROM profesionales WHERE cuil=%s"
        cursor.execute(sql,(cuil_el,))
        conexion.commit()

def listado_profesionales():
     cursor, conexion = conectar()
     cursor.execute("SELECT * from profesionales LIMIT 10")
     profesionales = cursor.fetchall()
     print("Listado de Profesionales:")
     for profesional in profesionales:
          print(profesional)