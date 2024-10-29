# gestion_usuarios.py

from utilidades import cargar_usuarios, guardar_usuarios, ordenar_usuarios, ver_ispc
from modelos import Usuario

def agregar_usuario():
    usuarios = cargar_usuarios()
    id_usuario = len(usuarios) + 1
    username = input("Ingrese el username: ")

    if username in usuarios:
        print("El usuario ya existe.")
        return

    password = input("Ingrese la contraseña: ")
    email = input("Ingrese el email: ")
    dni = input("Ingrese el DNI: ")
    usuario = Usuario(id_usuario, dni, username, password, email)
    usuarios[username] = usuario
    guardar_usuarios(usuarios)

    print(f'Usuario {username} agregado con éxito.')

def modificar_usuario():
    usuarios = cargar_usuarios()
    username = input("Ingrese el username del usuario a modificar: ")

    if username not in usuarios:
        print("Usuario no encontrado.")
        return

    password = input("Ingrese la nueva contraseña: ")
    email = input("Ingrese el nuevo email: ")
    dni = input("Ingrese el nuevo DNI: ")

    usuarios[username].password = password
    usuarios[username].email = email
    usuarios[username].dni = dni
    guardar_usuarios(usuarios)

    print(f"Usuario {username} modificado con éxito.")

def eliminar_usuario():
    usuarios = cargar_usuarios()
    username = input("Ingrese el username del usuario a eliminar: ")

    if username not in usuarios:
        print("Usuario no encontrado.")
        return

    del usuarios[username]
    guardar_usuarios(usuarios)

    print(f"Usuario {username} eliminado con éxito.")

def buscar_usuario():
    usuarios = cargar_usuarios()
    username = input("Ingrese el username a buscar: ")

    if username in usuarios:
        print(usuarios[username])
    else:
        print("Usuario no encontrado.")

def mostrar_usuarios():
    usuarios = cargar_usuarios()
    while True:
        print("1. Mostrar usuarios sin ordenar")
        print("2. Ordenar usuarios")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                ver_ispc()
            break
        
        elif opcion == "2":
            print("Para ordenar por burbuja ingrese 'b'")
            print("Para ordenar por Python ingrese 'p'")
            x = input("Ingrese una opción de ordenamiento: ")
            
            if x in ["b", "p"]:
                ordenar_usuarios(x)
                ver_ispc()
            else:
                print("Opción de ordenamiento no válida.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
