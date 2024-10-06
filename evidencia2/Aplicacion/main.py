# main.py

from gestion_usuarios import agregar_usuario, modificar_usuario, eliminar_usuario, buscar_usuario, mostrar_usuarios
from gestion_accesos import registrar_acceso

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos los Usuarios")
        print("6. Ingresar al Sistema")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            modificar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            buscar_usuario()
        elif opcion == '5':
            mostrar_usuarios()
        elif opcion == '6':
            registrar_acceso()
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()