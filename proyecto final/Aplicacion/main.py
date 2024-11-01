# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestion_usuarios import agregar_usuario, modificar_usuario, eliminar_usuario, mostrar_usuarios, buscar_usuariov2
from gestion_accesos import registrar_acceso
from datos_pluviales import datos_pluviales
from DB.menu_db import menu_db

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al Sistema con los Datos de Usuario")
        print("3. Análisis de Datos")
        print("4. Salir de la aplicación")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_usuarios_accesos()
        elif opcion == '2':
            ingresar_sistema()
        elif opcion == '3':
            analisis_datos()
        elif opcion == '4':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def menu_usuarios_accesos():
    while True:
        print("\nMenú de Usuarios y Accesos:")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos los Usuarios")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            modificar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            buscar_usuariov2()
        elif opcion == '5':
            mostrar_usuarios()
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intente de nuevo.")

def ingresar_sistema():
    registrar_acceso()
    menu_db()

def analisis_datos():
    datos_pluviales()

if __name__ == "__main__":
    menu_principal()
