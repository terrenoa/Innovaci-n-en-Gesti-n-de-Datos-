# utilidades.py

import pickle

def cargar_usuarios():
    try:
        with open('usuarios.ispc', 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return {}

def guardar_usuarios(usuarios):
    with open('usuarios.ispc', 'wb') as f:
        pickle.dump(usuarios, f)

def cargar_accesos():
    try:
        with open('accesos.ispc', 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

def guardar_accesos(acceso):
    accesos = cargar_accesos()
    accesos.append(acceso)

    with open('accesos.ispc', 'wb') as f:
        pickle.dump(accesos, f)


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







def busqueda_secuencial(usuarios, username):
    print("Busqueda realizada por tecnica de busqueda secuencial.")
    
    if username in usuarios:
        return usuarios[username]  
    else:
        return None 


def busqueda_binaria(usuarios, username):
    print("Busqueda realizada por tecnica de bsqueda binaria")
    usernames = list(usuarios.keys())  
    inicio = 0
    fin = len(usernames) - 1

    while inicio <= fin:
        mid = (inicio + fin) // 2
        if usernames[mid] == username:
            return usuarios[usernames[mid]]
        elif usernames[mid] < username:
            inicio = mid + 1
        else:
            fin = mid - 1

    return None  #por si no encuentra 


def buscar_usuariov2():
    username = input("Escribe el usuario a buscar:")
    metodo = input("Elige el tipo de metodo: 1 para secuencial y 2 para el metodo binario: ")
    usuarios = cargar_usuarios()

    if not usuarios:
        print("No se encontraron usuarios en el archivo.")
        return None
    
    
    #ELEGIR MODO
    if metodo == '1':
        resultado = busqueda_secuencial(usuarios, username)
    elif metodo == '2':
        usuarios_ordenados = ordenar_python(usuarios) # NECESARIO PARA EL METODO BINARIO
        resultado = busqueda_binaria(usuarios_ordenados, username)
    else:
        print("Metodo de búsqueda no valido.")
        return None
    
    if resultado:
        print(f"Usuario encontrado: {resultado}")
    else:
        print("Usuario no encontrado.")
# prueb

'''
username = input("Escribe el usuario a buscar:")
metodo = input("Elige el tipo de metodo: 1 para secuencial y 2 para el metodo binario: ")


usuario = buscar_usuario(username, metodo)
print(usuario)
'''