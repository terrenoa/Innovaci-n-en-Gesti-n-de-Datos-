usuarios = {}

   

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    clave = input("clave: ")

    usuarios[nombre_usuario] = {
    'nombre': nombre,
    'apellido': apellido,
    'dni': dni,
    'correo': correo,
    'fecha_nacimiento': fecha_nacimiento,
    'clave': clave }


registrar_usuario()
registrar_usuario()


print(usuarios)