import mysql.connector
from mysql.connector import Error
from .conexionbd import conectar
from .crud_pacientes import gestiones_para_pacientes
from .crud_profesionales import gestiones_para_profesionales
from .curd_obrasocial import obras_sociales
from .turnero import turnero




def menu_db():
    conectar()
    while True:    
        print("\n")
        print("*"*3+" Menu De Base De Datos "+"*"*3)
        print("Por favor, eliga una de las siguientes opciones para continuar:")
        print("1. Menu Pacientes.")
        print("2. Menu Profesionales.")
        print("3. Menu Obras Sociales")
        print("4. Turnero")
        print("5. Regresar.")
        
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            gestiones_para_pacientes()
        elif opcion == "2":
            gestiones_para_profesionales()
        elif opcion == "3":
            obras_sociales()
        elif opcion == "4":
            turnero()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")
            

