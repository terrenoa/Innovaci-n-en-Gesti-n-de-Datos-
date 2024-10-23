
import random
import csv
import os
import matplotlib.pyplot as plt

#datos aleatorios:
def generar_datos_pluviales():
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    datos_anuales = []

    for dias in dias_en_mes:
        mes = [random.randint(0, 100) for _ in range(dias)]  # genera lluvia aleatoria entre 0 y 100 mm
        datos_anuales.append(mes)
    print(datos_anuales)
    return datos_anuales

# para guardarl ocomo archivos
def guardar_csv(datos_anuales, año):
    archivo_csv = f"registro_pluvial_{año}.csv"
    
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])

        # escribe los datos día a día
        for dia in range(31): 
            fila = []
            for mes in range(12):  
                if dia < len(datos_anuales[mes]):  # si el día existe en ese mes:
                    fila.append(datos_anuales[mes][dia])
                else:
                    fila.append('')  # si el día no existe (para meses con menos de 31 dias)
            writer.writerow(fila)  # escribe la fila completa (1 por día)

    print(f"Archivo {archivo_csv} guardado correctamente.")

def leer_csv(archivo):
    with open(archivo, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # omite la primera fila (los meses)
        # convertir a float:
        datos = []
        for row in reader:
            fila = [float(valor) if valor else 0.0 for valor in row]
            datos.append(fila)
        #agrupar datos
        datos_mensuales = []
        for mes in range(12):
            datos_mensuales.append([datos[d][mes] for d in range(len(datos))])
        return datos_mensuales

def mostrar_datos_mes(datos_anuales, mes):
    print(f"Datos de lluvia para el mes {mes + 1}:")
    for dia, lluvia in enumerate(datos_anuales[mes]):
        print(f"Día {dia + 1}: {lluvia} mm")

def generar_graficos(datos_anuales):
    lluvia_total_mensual = [sum(mes) for mes in datos_anuales]
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    # grafico de barras
    plt.bar(meses, lluvia_total_mensual)
    plt.title('Lluvias anuales')
    plt.xlabel('Mes')
    plt.ylabel('Milímetros de lluvia')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # grafico de dispersion
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    plt.figure(figsize=(10, 5))
    for mes_idx, mes in enumerate(meses):
        dias = range(1, dias_por_mes[mes_idx] + 1) 
        lluvia_del_mes = datos_anuales[mes_idx]
        
        # verifica que la cantidad de dias sea igual a la cantidad de datos de lluvia
        if len(lluvia_del_mes) > 0:  # Aseguramos que haya datos de lluvia
            plt.scatter([mes_idx + 1] * len(lluvia_del_mes), list(range(1, len(lluvia_del_mes) + 1)), 
                        c=lluvia_del_mes, cmap='viridis', alpha=0.6, label=mes)

    plt.title('Lluvia diaria por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Día del Mes')
    plt.colorbar(label='Milímetros de lluvia')
    plt.xticks(range(1, 13), meses, rotation=45)
    plt.grid(True)
    plt.legend(meses, loc='upper right')
    plt.tight_layout()
    plt.show() 

    # grafico de torta
    plt.pie(lluvia_total_mensual, labels=meses, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de lluvias por mes')
    plt.show()

def datos_pluviales():
    año = input("Ingrese el año de la consulta de datos: ")
    archivo_csv = f"registro_pluvial_{año}.csv"

    if os.path.exists(archivo_csv):
        print(f"El archivo para el año {año} fue encontrado.")
        datos_anuales = leer_csv(archivo_csv)
    else:
        print(f"El archivo para el año {año} no fue encontrado. Generando datos aleatorios...")
        datos_anuales = generar_datos_pluviales()
        guardar_csv(datos_anuales, año)

    # pedir que mes
    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
    mostrar_datos_mes(datos_anuales, mes)

    # generar garficos
    generar_graficos(datos_anuales)
