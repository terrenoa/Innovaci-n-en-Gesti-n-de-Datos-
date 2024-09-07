import random #para captcha
import re #para validador de contraseñas
import aritmetica
import captcha
import validador_contraseñas



usuarios = {}

#coleccion de usuarios de prueba
usuarios = {'pepitoL': {'nombre': 'Pepe', 'apellido': 'Lorenzati', 'dni': '46508945', 'correo': 'peep@gmasdm.c', 'fecha_nacimiento': '18/06/2205', 'clave': '123456'},
            'pepito23': {'nombre': 'Pepe3', 'apellido': 'Lorenzati', 'dni': '46508945', 'correo': 'peep@gmasdm.c', 'fecha_nacimiento': '18/06/2205', 'clave': '123456'}}


#funcion principal
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
             

#yo lo sacaria en un archivo aparte
def registrar_usuario():
#pedir datos
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su DNI: ")
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
    nombre_usuario = input("Ingrese su nombre de usuario: ")

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
        print (a)

#registro del usuario en el diccionario
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

