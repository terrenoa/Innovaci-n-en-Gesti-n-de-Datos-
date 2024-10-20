# gestion_accesos.py

from datetime import datetime
from utilidades import cargar_usuarios, guardar_accesos, cargar_accesos
from acceso import Acceso

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
