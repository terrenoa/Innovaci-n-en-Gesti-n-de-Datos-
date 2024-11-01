import random
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
    os.makedirs(path, exist_ok=True)  # Crea la carpeta si no existe
    archivo_csv = os.path.join(path, f"registro_pluvial_{año}.csv")
    df.to_csv(archivo_csv, index=False)
    print(f"Archivo {archivo_csv} guardado correctamente.")

# Leer el archivo CSV y cargarlo como DataFrame
def leer_csv(archivo):
    return pd.read_csv(archivo)

# Mostrar los datos de un mes específico
def mostrar_datos_mes(df, mes):
    print(f"Datos de lluvia para el mes {df.columns[mes]}:")
    print(df[df.columns[mes]].dropna())  # Mostrar solo los valores no nulos

# Generar gráficos
'''
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
'''

# Grafico de barras para lluvias anuales
def generar_grafico_barras(df, año):
    lluvia_total_mensual = df.sum()  
    meses = df.columns

    plt.bar(meses, lluvia_total_mensual)
    plt.title(f'Lluvias Anuales - {año}')
    plt.xlabel('Mes')
    plt.ylabel('Milímetros de lluvia')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # guarda el grafico en la carpeta datos analizas
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
    os.makedirs(path, exist_ok=True)
    plt.savefig(os.path.join(path, f"barras_anuales_{año}.png"))
    plt.show()

# Grafico de dispersion para lluvias diarias por mes
def generar_grafico_dispersión(df, año):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
    os.makedirs(path, exist_ok=True)

    for mes_idx, mes in enumerate(df.columns):
        dias = range(1, len(df[mes].dropna()) + 1)  # Solo los dias con datos
        plt.scatter([mes_idx + 1] * len(dias), df[mes].dropna(), label=mes)
        
    plt.title('Dispersión de Lluvias Diarias por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Precipitación (mm)')
    plt.xticks(ticks=range(1, 13), labels=df.columns, rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(path, f"dispersión_anual_{año}.png"))
    plt.show()

# Grafico circular para lluvias anual
def generar_grafico_circular_anual(df, año):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
    os.makedirs(path, exist_ok=True)

    lluvia_total_mensual = df.sum()  
    meses = df.columns

    plt.pie(lluvia_total_mensual, labels=meses, autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribución de Lluvias por Mes - {año}')
    plt.savefig(os.path.join(path, f"circular_anual_{año}.png"))
    plt.show()

# Grafico circular para un mes o
def generar_grafico_circular_mes(df, mes):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
    os.makedirs(path, exist_ok=True)
    
    
    plt.pie(df[df.columns[mes]].dropna(), autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribución de Lluvias para {df.columns[mes]}')
    plt.savefig(os.path.join(path, f"circular_{df.columns[mes]}.png"))
    plt.show()



def datos_pluviales_panda():
    
    año = input("Ingrese el año de la consulta de datos: ")
    archivo_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados", f"registro_pluvial_{año}.csv")

    
    if os.path.exists(archivo_csv):
        print(f"El archivo para el año {año} fue encontrado.")
        df = pd.read_csv(archivo_csv)
    else:
        print(f"El archivo para el año {año} no fue encontrado. Generando datos aleatorios...")
        df = generar_datos_pluviales()  # Generar datos si el archivo no existe
        guardar_csv(df, año)  

    # Análisis anual
    print("Análisis de Datos Anuales:")
    print(f"Máxima precipitación anual: {df.max().max()} mm")
    print(f"Mínima precipitación anual: {df.min().min()} mm")
    print(f"Promedio de precipitación anual: {df.mean().mean()} mm")

    # Generar gráficos anuales
    generar_grafico_barras(df, año)
    generar_grafico_dispersión(df, año)
    generar_grafico_circular_anual(df, año)

    # Pedir al usuario el mes
    mes = int(input("Ingrese el número del mes (1-12): ")) - 1

    # Análisis mensual
    print(f"\nAnálisis de Datos para {df.columns[mes]}:")
    mes_data = df[df.columns[mes]].dropna()  # Filtrar días válidos del mes
    print(f"Máxima precipitación del mes: {mes_data.max()} mm")
    print(f"Mínima precipitación del mes: {mes_data.min()} mm")
    print(f"Promedio de precipitación del mes: {mes_data.mean()} mm")

    # Generar gráfico circular para el mes específico
    generar_grafico_circular_mes(df, mes)

