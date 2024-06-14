# turnero.py
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



def turno():
        # Consulta SQL
    dni_in = input("Ingrese el DNI: ")
    sql= ''' SELECT especialidad.nombre,
    especialidad.idEspecialidad
    FROM pacientes
    JOIN obras ON pacientes.ObraS_idObraS = obras.idOS
    JOIN obras_has_especialidad ON obras.idOS = obras_has_especialidad.ObraS_idOS
    JOIN especialidad ON obras_has_especialidad.Especialidad_idEspecialidad = especialidad.idEspecialidad
    WHERE pacientes.dni = %s
    '''

    cursor.execute(sql, (dni_in,))
    resultados = cursor.fetchall()  

    print( ("-"*25), "Especialidades que cubre la obra social del paciente", ("-"*25))

    for resultado in resultados:
        print(f"-{resultado}")
    
    idEspe_seleccion = int(input("Ingrese el id de la especialidad: "))
    sql = '''SELECT profesionales.nombre, profesionales.idProfesionales
    FROM profesionales_has_especialidad
    JOIN profesionales ON profesionales_has_especialidad.Profesionales_idProfesionales = profesionales.idProfesionales
    WHERE profesionales_has_especialidad.Especialidad_idEspecialidad = %s
    '''
    cursor.execute(sql, (idEspe_seleccion,))
    resultados = cursor.fetchall()  

    print( ("-"*25), "Profesionales de esta especialidad: ", ("-"*25))

    for resultado in resultados:
        print(f"-{resultado}")

    idProf_seleccion = int(input("Ingrese el id del profesional: "))

    f_in = input("Ingrese la fecha del turno (AAAA-MM-DD): ")
    h_in = input("Ingrese la hora del turno (HH:MM): ")
    f_h = f_in +" "+ h_in
    sql = '''
    INSERT INTO turno (Pacientes_dni, Profesionales_idProfesionales, Especialidad_idEspecialidad, f_hora) VALUES (%s, %s, %s, %s)
    '''
    
    cursor.execute(sql, (dni_in, idProf_seleccion, idEspe_seleccion, f_h,))
    conexion.commit()

def buscar_turno_dni():
    dni_in = int(input("Ingrese el DNI a buscar: "))
    sql = ''' 
    SELECT t.idTurno, t.Pacientes_dni, p.nombre AS Paciente, t.Profesionales_idProfesionales, 
           pr.apellido AS Profesional, t.Especialidad_idEspecialidad, e.nombre AS Especialidad,
           f_hora
    FROM turno t
    JOIN pacientes p ON t.Pacientes_dni = p.dni
    JOIN profesionales pr ON t.Profesionales_idProfesionales = pr.idProfesionales
    JOIN especialidad e ON t.Especialidad_idEspecialidad = e.idEspecialidad
    WHERE t.Pacientes_dni = %s
    '''
    cursor.execute(sql, (dni_in,))
    resultados = cursor.fetchall()

    if resultados:
        print("-" * 25, "Turnos encontrados", "-" * 25)
        for resultado in resultados:
            print(f"ID Turno: {resultado[0]}, Paciente: {resultado[1]}, "
                  f"Profesional: {resultado[4]}, Especialidad: {resultado[6]}, "
                  f"Fecha del turno: {resultado[7]}")
    else:
        print("No se encontraron turnos para el DNI ingresado.")

def list_turno():
    fecha1 = input("Ingrese la fecha (AAAA-MM-DD) desde iniciar la busqueda del turno: ")
    fecha2 = input("Ingrese la fecha (AAAA-MM-DD) hasta donde debe llegar la consulta: ")
    sql = ''' 
    SELECT t.idTurno, t.Pacientes_dni, p.nombre AS Paciente, t.Profesionales_idProfesionales, 
           pr.apellido AS Profesional, t.Especialidad_idEspecialidad, e.nombre AS Especialidad,
           f_hora
    FROM turno t
    JOIN pacientes p ON t.Pacientes_dni = p.dni
    JOIN profesionales pr ON t.Profesionales_idProfesionales = pr.idProfesionales
    JOIN especialidad e ON t.Especialidad_idEspecialidad = e.idEspecialidad
    WHERE f_hora BETWEEN %s AND %s
    '''
    cursor.execute(sql, (fecha1, fecha2,))
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(f"-{resultado}")

def turnero():
    # Implementación de la función
    print("\n"*3)
    print("Turnero")

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Crear Turno')
        print('2. Buscar Turno por DNI')
        print('3. Listado de Turnos por fecha')
        print('4. Salir')
    
        option_pac = input('Ingrese la opción deseada: ')
    
        if option_pac == '1':
            print("\n")
            turno()


        elif option_pac == '2':
           print("\n")
           buscar_turno_dni()
    

        elif option_pac == '3':
            print("\n")
            print(("*")*25,"TURNOS",("*")*25)
            list_turno()
            print("\n")
            
    
        elif option_pac == '4':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')


