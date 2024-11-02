import os
from datetime import datetime
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
#esta funcion queda obsoleta con la implementacion de ordenar por username y que usuarios ispc este siempre por dni
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

def ver_ispc_ordenados_usuario():

    try:
        with open('usuariosOrdenadosPorUsername.ispc', 'rb') as f:
            usuarios = pickle.load(f)
    except (FileNotFoundError, EOFError):
        print("error")
    
    
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
    opcion = input("¿Buscar por (1) Username, (2) DNI, (3) Email? ")
    
    if opcion == '1':
        username = input("Ingrese el username a buscar: ")
        encontrado, intentos = buscar_usuario_por_username(username)
        if not encontrado:
            print("No se encontró el usuario con dicho username.")
    
    elif opcion == '2':
        dni = input("Ingrese el DNI a buscar: ")
        buscar_usuario_por_dni(dni)
    
    elif opcion == '3':
        email = input("Ingrese el email a buscar: ")
        buscar_usuario_por_email(email)
    
    else:
        print("Opción no válida.")


#----------------------------------------------------------------------#
# Ordenamiento por username

def guardar_usuarios_ordenados_por_username(usuarios):
    # Guardar los usuarios en un nuevo archivo ordenados por username
    with open('usuariosOrdenadosPorUsername.ispc', 'wb') as f:
        pickle.dump(usuarios, f)

# Ordenamiento usando burbuja (por username)
def ordenar_burbuja_por_username(usuarios):
    usernames = list(usuarios.keys())
    n = len(usernames)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if usernames[j] > usernames[j + 1]:
                # Intercambiar los usernames
                usernames[j], usernames[j + 1] = usernames[j + 1], usernames[j]
    
    # Reconstruir el diccionario ordenado por username
    usuarios_ordenados = {username: usuarios[username] for username in usernames}
    return usuarios_ordenados

# Función para gestionar la opción de ordenamiento por username
def ordenar_usuarios_por_username():
    usuarios = cargar_usuarios()
    
    if not usuarios:
        print("No hay usuarios para ordenar.")
        return
    
    # Ordenar los usuarios por username usando burbuja
    usuarios_ordenados = ordenar_burbuja_por_username(usuarios)
    print("Usuarios ordenados por técnica de burbuja (por username).")
    
    # Guardar los usuarios ordenados en 'usuariosOrdenadosPorUsername.ispc'
    guardar_usuarios_ordenados_por_username(usuarios_ordenados)
    print("Usuarios ordenados y guardados en 'usuariosOrdenadosPorUsername.ispc'.")

#----------------------------------------------------------------------------
#funcion que se implementa en el main

def mostrar_usuarios():
    usuarios = cargar_usuarios()
    while True:
        print("1. Mostrar usuarios ordenados por DNI")
        print("2. Mostrar usuarios ordenados por username")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                ver_ispc()
            break
        
        elif opcion == "2":
            ordenar_usuarios_por_username()
            ver_ispc_ordenados_usuario()

#----------------------------------------

def cargar_usuarios_ordenados_por_username():
    # Supongamos que estás cargando usuarios desde un archivo usando pickle
    import pickle
    
    # Cargar usuarios desde el archivo
    with open('usuariosordenadosporusername.ispc', 'rb') as file:
        usuarios_dict = pickle.load(file)
    
    # Convertir el diccionario a una lista
    usuarios_ordenados = list(usuarios_dict.values())
    
    # Ordenar la lista por username (opcional, si ya está ordenada)
    usuarios_ordenados.sort(key=lambda usuario: usuario.username)

    return usuarios_ordenados

carpeta_busquedas = os.path.dirname(os.path.abspath(__file__)) + "/busquedasYordenamientos"
if not os.path.exists(carpeta_busquedas):
    os.makedirs(carpeta_busquedas)

def buscar_usuario_por_username(username):
    usuarios = cargar_usuarios()  # Cargar usuarios de tu archivo
    intentos = 0
    log_file_path = os.path.join(carpeta_busquedas, f'buscandoUsuarioPorUsername-{datetime.now().strftime("%Y%m%d-%H%M%S")}.txt')

    # Abrir el archivo de log antes de comenzar la búsqueda
    with open(log_file_path, 'a') as log:
        log.write(f"Búsqueda por Username: buscando el username '{username}'.\n")

        # Verificar si existe el archivo de usuarios ordenados
        if os.path.exists("usuariosOrdenadosPorUsername.ispc"):
            usuarios_ordenados = cargar_usuarios_ordenados_por_username()
            intentos, encontrado = busqueda_binaria_username(usuarios_ordenados, username, log_file_path, intentos)
            if encontrado:
                return True, intentos
            else:
                log.write(f"Usuario no encontrado usando búsqueda binaria.\n")
                print(f"Usuario no encontrado usando búsqueda binaria.")

        # Si no se encontró, intentar búsqueda secuencial en el archivo original
        log.write(f"Buscando el username '{username}' en el archivo original con búsqueda secuencial...\n")
        for usuario in usuarios.values():
            intentos += 1
            log.write(f"Intento {intentos}: Comparando '{username}' con '{usuario.username}'.\n")
            print(f"Intento {intentos}: '{username}' es distinto a '{usuario.username}'")
            if usuario.username == username:
                print(f"Usuario encontrado: {usuario}")
                log.write(f"Username encontrado en {intentos} intentos.\n")
                return True, intentos

        print("Usuario no encontrado.")
        log.write(f"Se realizaron {intentos} intentos y no se encontró el username buscado.\n")
    return False, intentos

def buscar_usuario_por_dni(dni):
    usuarios = cargar_usuarios()
    intentos = 0
    usuarios_ordenados = sorted(usuarios.values(), key=lambda x: x.dni)
    log_file = os.path.join(carpeta_busquedas, f'buscandoUsuarioPorDNI-{datetime.now().strftime("%Y%m%d-%H%M%S")}.txt')

    with open(log_file, 'w') as log:
        log.write(f"Búsqueda Binaria por DNI: buscando el DNI '{dni}' en el archivo usuarios.ispc que contiene {len(usuarios_ordenados)} usuarios.\n")

        if not usuarios_ordenados:
            print("No hay usuarios registrados.")
            return

        if dni < usuarios_ordenados[0].dni:
            print(f"No se encuentra registrado el usuario con el DNI '{dni}' debido a que el DNI a buscar es más chico que el más chico de los registrados.")
            return
        if dni > usuarios_ordenados[-1].dni:
            print(f"No se encuentra registrado el usuario con el DNI '{dni}' debido a que el DNI a buscar es más grande que el más grande de los registrados.")
            return

        inicio, fin = 0, len(usuarios_ordenados) - 1
        while inicio <= fin:
            mid = (inicio + fin) // 2
            valor_campo = usuarios_ordenados[mid].dni
            intentos += 1
            log.write(f"Intento {intentos}: DNI del usuario de la posición {mid} es {valor_campo}.\n")

            if valor_campo == dni:
                print(f"Usuario encontrado: {usuarios_ordenados[mid]}")
                log.write(f"DNI encontrado en {intentos} intentos.\n")
                return True, intentos
            elif valor_campo < dni:
                log.write(f"Buscar en la subsecuencia de la derecha (posición {mid + 1} a {fin}).\n")
                inicio = mid + 1
            else:
                log.write(f"Buscar en la subsecuencia de la izquierda (posición {inicio} a {mid - 1}).\n")
                fin = mid - 1

        log.write(f"Se realizaron {intentos} intentos y no se encontró el DNI buscado.\n")
        print("Usuario no encontrado.")
        return False, intentos


def buscar_usuario_por_email(email):
    usuarios = cargar_usuarios()
    intentos = 0
    print(f"Buscando el email '{email}'...")

    for usuario in usuarios.values():
        intentos += 1
        print(f"Intento {intentos}: Comparando con '{usuario.email}'")
        if usuario.email == email:
            print(f"Usuario encontrado: {usuario}")
            return True, intentos
    
    print("Usuario no encontrado.")
    return False, intentos



#################

def busqueda_binaria_username(usuarios_ordenados, username, log_file, intentos):
    inicio, fin = 0, len(usuarios_ordenados) - 1
    with open(log_file, 'a') as log:
        log.write(f"Búsqueda Binaria por Username: buscando el username '{username}'.\n")
        
        while inicio <= fin:
            mid = (inicio + fin) // 2
            valor_campo = usuarios_ordenados[mid].username
            intentos += 1
            
            # Escribir en el log
            log.write(f"Intento {intentos}: username del usuario de la posición {mid} es '{valor_campo}'.\n")
            
            # Imprimir en la consola
            print(f"Intento {intentos}: username del usuario de la posición {mid} es '{valor_campo}'.")

            if valor_campo == username:
                print(f"Usuario '{username}' encontrado en el intento {intentos}.")
                return intentos, True
            elif valor_campo < username:
                log.write(f"Buscar en la subsecuencia de la derecha (posición {mid + 1} a {fin}).\n")
                print(f"Buscar en la subsecuencia de la derecha (posición {mid + 1} a {fin}).")
                inicio = mid + 1
            else:
                log.write(f"Buscar en la subsecuencia de la izquierda (posición {inicio} a {mid - 1}).\n")
                print(f"Buscar en la subsecuencia de la izquierda (posición {inicio} a {mid - 1}).")
                fin = mid - 1

    print(f"Usuario '{username}' no encontrado después de {intentos} intentos.")
    return intentos, False


