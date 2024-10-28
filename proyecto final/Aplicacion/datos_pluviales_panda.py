import random
import os
import pandas as pd
import matplotlib.pyplot as plt

# Genera los datos de forma aleatoria, un dato por día en un año
def generar_datos_pluviales():
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    # Inicializamos un diccionario vacío para los datos
    datos = {}
    
    # Generamos los datos mes por mes
    for i in range(12):
        mes = []  # Lista para almacenar los datos de cada mes
        for j in range(31):
            if j < dias_en_mes[i]:  # Si el día existe en el mes
                mes.append(random.uniform(0, 100))  # Genera lluvia aleatoria
            else:
                mes.append(None)  # Si el día no existe, añade None
        datos[meses[i]] = mes  # Asignamos la lista del mes al diccionario
    
    # Convertimos a un DataFrame de Pandas
    df = pd.DataFrame(datos)
    
    return df

# Guardar el DataFrame en CSV
def guardar_csv(df, año):
    archivo_csv = f"registro_pluvial_{año}.csv"
    df.to_csv(archivo_csv, index=False)  # Guardar sin índices adicionales
    print(f"Archivo {archivo_csv} guardado correctamente.")

# Leer el archivo CSV y cargarlo como DataFrame
def leer_csv(archivo):
    return pd.read_csv(archivo)

# Mostrar los datos de un mes específico
def mostrar_datos_mes(df, mes):
    print(f"Datos de lluvia para el mes {df.columns[mes]}:")
    print(df[df.columns[mes]].dropna())  # Mostrar solo los valores no nulos

# Generar gráficos
def generar_graficos(df):
    # Gráfico de barras
    lluvia_total_mensual = df.sum()
    meses = df.columns
    
    # Gráfico de barras
    plt.bar(meses, lluvia_total_mensual)
    plt.title('Lluvias anuales')
    plt.xlabel('Mes')
    plt.ylabel('Milímetros de lluvia')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Gráfico circular
    plt.pie(lluvia_total_mensual, labels=meses, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de lluvias por mes')
    plt.show()

def datos_pluviales_panda():
    año = input("Ingrese el año de la consulta de datos: : ")
    archivo_csv = f"registro_pluvial_{año}.csv"

    # Verificar si el archivo CSV existe
    if os.path.exists(archivo_csv):
        print(f"El archivo para el año {año} fue encontrado.")
        df = leer_csv(archivo_csv)
    else:
        print(f"El archivo para el año {año} no fue encontrado. Generando datos aleatorios...")
        df = generar_datos_pluviales()
        guardar_csv(df, año)

    # Pedir al usuario el mes
    mes = int(input("Ingrese el número del mes (1-12): ")) - 1
    mostrar_datos_mes(df, mes)

    # Generar gráficos
    generar_graficos(df)
