def suma(v1,v2):
    vt= float(v1 + v2)
    return round(vt,2)

def resta(v1,v2):
    vt= float(v1 - v2)
    return round(vt,2)

def mult(v1,v2):
    vt= float(v1 * v2)
    return round(vt,2)

def div(v1,v2):
    if v2 == 0:
        print( "ERROR ERROR ERROR")
        print ("no se puede dividir ntre 0")
    else:
        vt= float(v1 / v2)
        return round(vt,2)

#definicion alternativa de la funcion div que aplica el uso de excepciones
'''
def div(v1,v2):
    try:
        return round((v1/v2),2)
    except:
        print("ERROR ERROR ERROR")
        print ("no se puede dividir entre 0")
'''
    
def sumar_n(*lista):
    return sum(lista)

def promedio(*lista):
    
    return sum(lista) / len(lista)



    

#a= promedio(1,1,1,1,1)
#print (a)
