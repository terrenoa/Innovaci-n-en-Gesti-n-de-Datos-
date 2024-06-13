# index_hospital.py

# Importa las funciones desde sus archivos individuales
from gestiones_para_pacientes import gestiones_para_pacientes 
from gestiones_para_profesionales import gestiones_para_profesionales
from servicios_medicos import servicios_medicos
from obras_sociales import obras_sociales
from turnero import turnero
import mysql.connector
from mysql.connector import Error

#inicializacion de variables
conexion = None
cursor = None


try:
    conexion = mysql.connector.connect(
           host="localhost",
           port=3306,
           user="root",
           password="85956123",
           db="mydb" 
    )
    if conexion.is_connected():
         print("Conexión exitosa a la base de datos")
         
except Error as ex:
      print("Error durante la conexion.", ex)

cursor = conexion.cursor()





def index_hospital():
    while True:
        print('******HOSPITAL HOSPITAL******')
        print('Bienvenido al programa de gestión hospitalaria')
        print('Elija una de las siguientes opciones:')
        print('1. Gestiones para pacientes')
        print('2. Gestiones para profesionales')
        print('3. Servicios médicos')
        print('4. Obras sociales')
        print('5. Turnero')
        print('6. Salir')
    
        option = input('Ingrese la opción deseada: ')
    
        if option == '1':
            print("\n")
            gestiones_para_pacientes()
        elif option == '2':
            print("\n")
            gestiones_para_profesionales()
        elif option == '3':
            print("\n")
            servicios_medicos()
        elif option == '4':
            print("\n")
            obras_sociales()
        elif option == '5':
            print("\n")
            turnero()
        elif option == '6':
            print("\n")
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')

# Ejecuta el programa principal
index_hospital()
