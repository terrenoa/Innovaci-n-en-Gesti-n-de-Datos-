# gestion_usuarios.py
import pickle
#from utilidades import cargar_usuarios, guardar_usuarios, ordenar_usuarios, ver_ispc
from modelos import Usuario

#Funciones Gestion Usuarios:

def cargar_usuarios():
    try:
        with open('usuarios.ispc', 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return {}

def guardar_usuarios(usuarios):
    usuarios_ordenados = dict(sorted(usuarios.items(), key=lambda item: item[1].dni))
    with open('usuarios.ispc', 'wb') as f:
        pickle.dump(usuarios_ordenados, f)




def ordenar_burbuja(usuarios):
    usernames = list(usuarios.keys())
    n = len(usernames)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if usernames[j] > usernames[j + 1]:
                # Intercambiar los usernames
                usernames[j], usernames[j + 1] = usernames[j + 1], usernames[j]
    
    # Reconstruir el diccionario ordenado
    usuarios_ordenados = {username: usuarios[username] for username in usernames}
    return usuarios_ordenados


# ordenamiento usando sort()
def ordenar_python(usuarios):
    # utiliza la clave de los usernames para ordenar
    usuarios_ordenados = dict(sorted(usuarios.items(), key=lambda item: item[0]))
    return usuarios_ordenados

# Función para gestionar la opción de ordenamiento
def ordenar_usuarios(opcion):
    usuarios = cargar_usuarios()
    
    if not usuarios:
        print("No hay usuarios para ordenar.")
        return
    
    if opcion == "b":
        usuarios_ordenados = ordenar_burbuja(usuarios)
        print("Usuarios ordenados por técnica de burbuja.")
    elif opcion == "p":
        usuarios_ordenados = ordenar_python(usuarios)
        print("Usuarios ordenados por el método sort() de Python.")
    else:
        print("Opción no válida.")
        return
    
    # Guardar los usuarios ordenados solo si se eligió ordenar
    guardar_usuarios(usuarios_ordenados)
    print("Usuarios ordenados y guardados en 'usuarios.ispc'.")

def ver_ispc():
    usuarios = cargar_usuarios()
    
    if not usuarios:
        print("El archivo 'usuarios.ispc' está vacío o no existe.")
    else:
        for username, datos in usuarios.items():
            print(f"Username: {username}, Datos: {datos}")







def busqueda_secuencial(usuarios, valor_busqueda, campo_busqueda): #campo_busqueda = username o dni o email
    print("Busqueda realizada por tecnica de busqueda secuencial.")
    
    for usuario in usuarios.values():
        if getattr(usuario, campo_busqueda) == valor_busqueda:
            return usuario
    return None


def busqueda_binaria(usuarios, valor_busqueda, campo_busqueda):
    print("Búsqueda realizada por técnica de búsqueda binaria")
    usuarios_ordenados = sorted(usuarios.values(), key=lambda x: getattr(x, campo_busqueda))  # Ordenar por el campo
    inicio = 0
    fin = len(usuarios_ordenados) - 1

    while inicio <= fin:
        mid = (inicio + fin) // 2
        valor_campo = getattr(usuarios_ordenados[mid], campo_busqueda)
        
        if valor_campo == valor_busqueda:
            return usuarios_ordenados[mid]
        elif valor_campo < valor_busqueda:
            inicio = mid + 1
        else:
            fin = mid - 1

    return None  # Por si no encuentra 


def buscar_usuariov2():
    campo_busqueda = input("Ingrese el campo de busqueda (username, dni o email): ")
    valor_busqueda = input("Escribe el usuario a buscar:")
    metodo = input("Elige el tipo de metodo: 1 para secuencial y 2 para el metodo binario: ")
    usuarios = cargar_usuarios()

    if not usuarios:
        print("No se encontraron usuarios en el archivo.")
        return None
    
    
    #ELEGIR MODO
    if metodo == '1':
        resultado = busqueda_secuencial(usuarios, valor_busqueda, campo_busqueda)
    elif metodo == '2':
        usuarios_ordenados = ordenar_python(usuarios) # NECESARIO PARA EL METODO BINARIO
        resultado = busqueda_binaria(usuarios_ordenados, valor_busqueda, campo_busqueda)
    else:
        print("Metodo de búsqueda no valido.")
        return None
    
    if resultado:
        print(f"Usuario encontrado: {resultado}")
    else:
        print("Usuario no encontrado.")



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
