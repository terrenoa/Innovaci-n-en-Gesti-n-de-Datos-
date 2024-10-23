import mysql.connector
from mysql.connector import Error

def conectar():
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
    return cursor, conexion

