import random
import aritmetica

def captcha():
    """
    Funcion que sirve para resolver un pequeño captcha,
    tienes que introducir el resultado de una suma de dos numeros aleatorios.
    """
    x = random.randint(1,10)
    y = random.randint(1,10)
    resp = 0
    print("PARA CONTINUAR RESUELVA EL CAPTCHA")
    resp = int(input(f"{x} + {y} = "))

    
    if resp == aritmetica.suma(x,y):
        return True
    else:
        print("ERROR, CAPTCHA INCORRECTO")
        captcha()
    
    
## help(captcha)