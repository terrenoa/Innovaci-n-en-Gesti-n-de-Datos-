# index_hospital.py

# Importa las funciones desde sus archivos individuales
from gestiones_para_pacientes import gestiones_para_pacientes
from gestiones_para_profesionales import gestiones_para_profesionales
from servicios_medicos import servicios_medicos
from obras_sociales import obras_sociales
from turnero import turnero

def index_hospital():
    while True:
        print('******HOSPITAL HOSPITAL******')
        print('Bienvenido al programa de gestión hospitalaria')
        print('Elija una de las siguientes opciones:')
        print('1. Gestiones para pacientes')
        print('2. Gestiones para profesionales')
        print('3. Servicios médicos')
        print('4. Obras sociales')
        print('5. Turnero')
        print('6. Salir')
    
        option = input('Ingrese la opción deseada: ')
    
        if option == '1':
            gestiones_para_pacientes()
        elif option == '2':
            gestiones_para_profesionales()
        elif option == '3':
            servicios_medicos()
        elif option == '4':
            obras_sociales()
        elif option == '5':
            turnero()
        elif option == '6':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')

# Ejecuta el programa principal
index_hospital()
