from datetime import datetime #FECHA Y HORA ACTUAl

def registrar_inicio_sesion(nombre_usuario):
    with open("logs.txt", "a") as archivo_logs:
        fecha_hora_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S") #
        archivo_logs.write(f"Usuario: {nombre_usuario} inicio sesion el {fecha_hora_actual}\n")

