import random
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

# Genera los datos de forma aleatoria, un dato por dia en un año
def generar_datos_pluviales():
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    datos_anuales = []  # se inicia vacia porque aca se van a ir agregando los datos mensuales

    for dias in dias_en_mes:
        mes = [random.uniform(0, 100) for _ in range(dias)]  # Genera lluvia aleatoria entre 0 y 100 mm
        datos_anuales.append(mes)
    print(datos_anuales)
    return datos_anuales

#para guardarlo como archivo
'''
def guardar_csv(datos_anuales, año):
    # crea un archivo con 12 columnas y 31 filas, conviene de esta forma porque es mas facil mostrar cuando se pide los datos de un solo mes
    archivo_csv = f"registro_pluvial_{año}.csv"
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
        for dia in range(31):  
            fila = [] 
            for mes in range(12): 
        # Verificamos si el día actual existe en el mes actual (algunos meses tienen menos de 31 días)
                if dia < len(datos_anuales[mes]):  
                    fila.append(datos_anuales[mes][dia])  # Si el día existe, añadimos el valor de lluvia
                else:
                    fila.append('')  # Si el día no existe, añadimos una cadena vacía
            writer.writerow(fila)
'''
def guardar_csv(datos_anuales, año):
    archivo_csv = f"registro_pluvial_{año}.csv"
    
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Encabezados
        writer.writerow(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
        
        # Escribir los datos día a día
        for dia in range(31):  # Recorre hasta 31 días
            fila = []
            for mes in range(12):  # Recorre los 12 meses
                if dia < len(datos_anuales[mes]):  # Si el día existe en el mes actual
                    fila.append(datos_anuales[mes][dia])
                else:
                    fila.append('')  # Si el día no existe (para meses con menos de 31 días)
            writer.writerow(fila)  # Escribe la fila completa (1 por día)

    print(f"Archivo {archivo_csv} guardado correctamente.")

    
def leer_csv(archivo):
    with open(archivo, newline='') as file:
        reader = csv.reader(file)
        return list(reader)
    
def mostrar_datos_mes(datos_anuales, mes):
    print(f"Datos de lluvia para el mes {mes + 1}:")
    for dia, lluvia in enumerate(datos_anuales[mes]):
        print(f"Día {dia + 1}: {lluvia} mm")

def generar_graficos(datos_anuales):
    # Gráfico de barras
    lluvia_total_mensual = [sum(mes) for mes in datos_anuales]
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    plt.bar(meses, lluvia_total_mensual)
    plt.title('Lluvias anuales')
    plt.xlabel('Mes')
    plt.ylabel('Milímetros de lluvia')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Gráfico de dispersión
    dias = range(1, 32)
    for mes_idx, mes in enumerate(meses):
        plt.scatter([mes_idx + 1] * len(dias), dias[:len(datos_anuales[mes_idx])], c=datos_anuales[mes_idx])
    plt.title('Lluvia diaria')
    plt.xlabel('Mes')
    plt.ylabel('Día')
    plt.colorbar(label='Milímetros de lluvia')
    plt.show()

    # Gráfico circular
    plt.pie(lluvia_total_mensual, labels=meses, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de lluvias por mes')
    plt.show()

def datos_pluviales():
    año = input("Ingrese el año de la consulta de datos: : ")
    archivo_csv = f"registro_pluvial_{año}.csv"

    # Verificar si el archivo CSV existe
    if os.path.exists(archivo_csv):
        print(f"El archivo para el año {año} fue encontrado.")
        datos_anuales = leer_csv(archivo_csv)
    else:
        print(f"El archivo para el año {año} no fue encontrado. Generando datos aleatorios...")
        datos_anuales = generar_datos_pluviales()
        guardar_csv(datos_anuales, año)

    # Pedir al usuario el mes
    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
    mostrar_datos_mes(datos_anuales, mes)

    # Generar gráficos
   # generar_graficos(datos_anuales)
