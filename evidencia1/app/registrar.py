import json #UTILIZAMOS LA LIBRERIA DE JAVA PARA CARGAR LOS ARCHiVOS .TXT DE MANERA MAS COMODA
import captcha
import validador_contraseñas

def cargar_usuarios(): ##ABRE EL ARCHIVO EN MODO LECTURA SOLAMENTE "r"
    with open("usuarios.txt", "r") as archivo:
        return json.load(archivo)

def guardar_usuarios(usuarios): ##ABRE EL ARCHIVO EN MODO ESCRITURA "w"
    with open("usuarios.txt", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def inicio_sesion():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    if nombre_usuario in usuarios: ##SI ENCUNETRA EL USUARIO...
        clave = input("Ingrese la contraseña: ")
        if usuarios[nombre_usuario]["clave"] == clave: 
            print("Bienvenido!!")
        else:
            print("CONTRASEÑA INCORRECTA!!\n")
            recovery = str(input("Olvido su contraseña? (Y/N)\n"))
            if recovery.lower() == "y":
                print("OPCION NO IMPLEMENTADA")
            else:
                print("\nAdios!!")
     
    else: ## SINO....
        print("usuario no econtrado: ")
        opcion = int(input ("para registrar ingrese 1: "))
        if opcion == 1:
            agregar_usuario()
        else:
             print("Adios!")
        


def agregar_usuario():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Ingrese el nuevo nombre de usuario: ")
# verifica si el usuario ya existe
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
        agregar_usuario()

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")


#peidr clave y validar
    clave = validador_contraseñas.pedir_contraseña()
    ctrl = validador_contraseñas.validar(clave)
    while ctrl == False:
        clave = validador_contraseñas.pedir_contraseña()
        ctrl = validador_contraseñas.validar(clave)
    
#verificacion con captcha
    a= False
    while a == False:
        a = captcha.captcha()
    
# guarda el usuario en el archivo de usuarios.txt!
    usuarios[nombre_usuario] = {"nombre": nombre, "apellido": apellido, "dni": dni, "correo": correo, "fecha_nacimiento": fecha_nacimiento, "clave": clave}
    guardar_usuarios(usuarios)
    print(f"Usuario {nombre_usuario} agregado exitosamente.")

inicio_sesion()
