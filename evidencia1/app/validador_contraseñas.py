import re

def pedir_contraseña():
    print("Requisitos de clave: ")
    print("• al menos 8 caracteres")
    print("• al menos 1 mayúscula")
    print("• al menos 1 número")
    print("• al menos un caracter especial")
    clave = input("clave: ")
    return clave



def validar(contraseña):
    # Verifica que la contraseña tenga al menos 8 caracteres
    if len(contraseña) < 8:
        print ("La contraseña debe tener al menos 8 caracteres.")
        return False

    # Condiciones a verificar
    minúscula = re.search(r'[a-z]', contraseña)  # Al menos 1 minúscula
    mayúscula = re.search(r'[A-Z]', contraseña)  # Al menos 1 mayúscula
    número = re.search(r'[0-9]', contraseña)     # Al menos 1 número
    especial = re.search(r'[\W_]', contraseña)   # Al menos 1 caracter especial (\W busca cualquier cosa que no sea letra o número)

    # Contar cuántas condiciones se cumplen
    condiciones_cumplidas = sum([bool(minúscula), bool(mayúscula), bool(número), bool(especial)])

    # Verifica si cumple con al menos 2 de las condiciones
    if condiciones_cumplidas >= 2:
        print( "Contraseña válida.")
        return True
    else:
        print ("La contraseña debe cumplir al menos 2 de las siguientes condiciones: minúscula, mayúscula, número o caracter especial.")
        return False

