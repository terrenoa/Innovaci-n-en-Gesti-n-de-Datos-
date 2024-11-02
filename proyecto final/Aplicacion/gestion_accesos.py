# gestion_accesos.py
import pickle
from datetime import datetime
from gestion_usuarios import cargar_usuarios
from acceso import Acceso

# Funciones Gestion de Acceso: 

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

def registrar_acceso():
    usuarios = cargar_usuarios()  # Asegurarse de cargar usuarios correctamente

    if not usuarios:
        print("No hay usuarios registrados. Por favor, cree un usuario primero.")
        return

    username = input("Ingrese el username: ")
    password = input("Ingrese la contraseña: ")

    # Verificar si el usuario existe y la contraseña es correcta
    if username in usuarios and usuarios[username].password == password:
        print("Ingreso exitoso.")
        
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id_acceso = len(cargar_accesos()) + 1
        acceso = Acceso(id_acceso, fecha_ingreso, None, username)
        guardar_accesos(acceso)
        
        print("Acceso registrado con éxito.")

        # Opción para salir del sistema o volver al menú principal
        while True:
            opcion = input("Ingrese 's' para salir o 'm' para volver al menú: ")
            if opcion == 's':
                print("Saliendo del sistema.")
                break
            elif opcion == 'm':
                return  # Volver al menú principal
            else:
                print("Opción no válida.")
    else:
        print("Usuario o contraseña incorrectos.")
        # Registrar intento fallido
        with open("logs.txt", "a") as log_file:
            log_file.write(f"{datetime.now()}: Intento fallido con usuario '{username}'\n")

def ver_accesos_ispc():
    try:
        with open('accesos.ispc', 'rb') as f:
            accesos = pickle.load(f)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
        return f"Error: No se pudo abrir o leer el archivo 'accesos.ispc'. Detalles: {e}"
    
    if not accesos:
        return "El archivo 'accesos.ispc' está vacío o no contiene datos válidos."
    else:
        output = []
        for acceso in accesos:
            output.append(f"Datos: {acceso}")
            print(output)
        return "\n".join(output)

def mostrar_logs():
    try:
        with open('logs.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                print(linea.strip())
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo 'logs.txt'.")