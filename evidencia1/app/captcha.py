import random
import aritmetica

def captcha():
    x = random.randint(1,10)
    y = random.randint(1,10)
    resp = None
    print("PARA CONTINUAR RESUELVA EL CAPTCHA")
    resp = int(input(f"{x} + {y} = "))
    if resp == aritmetica.suma(x,y):
        return True
    else:
        return False

#a= False
#while a == False:
#    a = captcha()
#    print (a)

