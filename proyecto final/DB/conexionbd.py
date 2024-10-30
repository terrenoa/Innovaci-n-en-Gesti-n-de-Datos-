import mysql.connector
from mysql.connector import Error

def conectar():
    conexion = None  # Define la variable 'conexion' fuera del bloque 'try'
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
            cursor = conexion.cursor()
            return cursor, conexion
    except Error as ex:
        print("Error durante la conexión, verifica las credenciales:", ex)
        
    return None, conexion  # Retorna 'None' para el cursor si hay error en la conexión


