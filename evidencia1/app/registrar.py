import random
import aritmetica
import captcha

usuarios = {}

usuarios = {'pepitoL': {'nombre': 'Pepe', 'apellido': 'Lorenzati', 'dni': '46508945', 'correo': 'peep@gmasdm.c', 'fecha_nacimiento': '18/06/2205', 'clave': '123456'},
            'pepito23': {'nombre': 'Pepe3', 'apellido': 'Lorenzati', 'dni': '46508945', 'correo': 'peep@gmasdm.c', 'fecha_nacimiento': '18/06/2205', 'clave': '123456'}}


def inicio_sesion():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    control = False
    for x in usuarios:
        if nombre_usuario == x:
            control = True
        else:
            control = False
    if control == False: #el usuario no existe
         print("usuario no econtrado: ")
         opcion = int(input ("para registrar ingrese 1: "))
         if opcion == 1:
             registrar_usuario()
             


def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    clave = input("clave: ")

    a= False
    while a == False:
        a = captcha.captcha()
        print (a)


    usuarios[nombre_usuario] = {
    'nombre': nombre,
    'apellido': apellido,
    'dni': dni,
    'correo': correo,
    'fecha_nacimiento': fecha_nacimiento,
    'clave': clave }
    print ("Usuario registrado con éxito!!")

inicio_sesion()
print(usuarios)

