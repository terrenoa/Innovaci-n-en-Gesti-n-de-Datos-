# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestion_usuarios import agregar_usuario, modificar_usuario, eliminar_usuario, mostrar_usuarios, buscar_usuariov2
from gestion_accesos import registrar_acceso
from datos_pluviales import datos_pluviales
from datos_pluviales_panda import datos_pluviales_panda
from DB.menu_db import menu_db
#from utilidades import buscar_usuariov2

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos los Usuarios")
        print("6. Ingresar al Sistema")
        print("7. NUEVO: Datos Pluviales")
        print("8. Base De Datos Del Hospital")
        print("9. Salir.")

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
            registrar_acceso()
        elif opcion == '7':
            datos_pluviales()
            #datos_pluviales_panda()
        elif opcion == '8':
            menu_db()
        elif opcion == '9':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()