import mysql.connector
from mysql.connector import Error
conexion = mysql.connector.connect(
           host="localhost",
           port=3306,
           user="root",
           password="74269851vV",
           db="mydb" 
)

cursor = conexion.cursor()


def crear_obras_espe(ObraS_idOS, Especialidad_idEspecialidad):
    sql = "INSERT INTO obras_has_especialidad (ObraS_idOS, Especialidad_idEspecialidad) VALUES ('{}', '{}')".format(ObraS_idOS, Especialidad_idEspecialidad)
    values = ()
    cursor.execute(sql)
    conexion.commit()

def eliminar_obras_espe():
    id_obras = input("Ingrese el id de la obra a eliminar de la relacion: ")
    id_espe = input("Ingrese el id de la especialidad: ")
    sql = "DELETE FROM obras_has_especialidad WHERE ObraS_idOS=%s and Especialidad_idEspecialidad=%s"
    cursor.execute(sql,(id_obras, id_espe))
    conexion.commit()

def list_obras_espe():
    # Consulta SQL para obtener los nombres de obras sociales y especialidades
    query = """
    SELECT 
        obras.nombre AS nombre_obra,
        especialidad.nombre AS nombre_especialidad
    FROM 
        obras
    JOIN 
        obras_has_especialidad ON obras.idOS = obras_has_especialidad.ObraS_idOS
    JOIN 
        especialidad ON obras_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad
    """

    cursor = conexion.cursor()  
    cursor.execute(query)  
    resultados = cursor.fetchall()  

    print( ("-"*25), "Especialidades por Obra Social", ("-"*25))
    for resultado in resultados:
        print(f"Obra Social: {resultado[0]}, Especialidad: {resultado[1]}")
    
    print("-"*82)
    
    cursor.close()

def obras_especialidad():
    print("\n")
    print("Obras-Especialidad")

    

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Agregar Relacion Obra Social-Especialidad')
        print('2. Eliminar Relacion ')
        print('3. Listado')
        print('4. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
            print("\n")
            obras_in = input("Ingrese el id de la Obra Social: ")
            espe_in = input("Ingrese el id de la Especialidad: ")
            crear_obras_espe(obras_in, espe_in)


        elif option_pac == '2':
           print("\n")
           eliminar_obras_espe()
    

        elif option_pac == '3':
            print("\n")
            list_obras_espe()
            print("\n")
            
    
        elif option_pac == '4':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')

