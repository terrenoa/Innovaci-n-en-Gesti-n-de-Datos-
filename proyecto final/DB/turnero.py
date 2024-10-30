from .conexionbd import conectar
import mysql.connector
from mysql.connector import Error

def turno():
    cursor, conexion = conectar()
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
    cursor.close()
    conexion.close()

def buscar_turno_dni():
    cursor, conexion = conectar()
    dni_in = int(input("Ingrese el DNI a buscar: "))
    sql = ''' 
    SELECT t.idTurno, t.Pacientes_dni, p.nombre AS Paciente, t.Profesionales_idProfesionales, 
           pr.apellido AS Profesional, t.Especialidad_idEspecialidad, e.nombre AS Especialidad,
           f_hora, estado
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
                  f"Fecha del turno: {resultado[7]}, "
                  f"Estado: {resultado[8]}.")
    else:
        print("No se encontraron turnos para el DNI ingresado.")
    cursor.close()
    conexion.close()

def list_turno():
    cursor, conexion = conectar()
    fecha1 = input("Ingrese la fecha (AAAA-MM-DD) desde iniciar la busqueda del turno: ")
    fecha2 = input("Ingrese la fecha (AAAA-MM-DD) hasta donde debe llegar la consulta: ")
    sql = ''' 
    SELECT t.idTurno, t.Pacientes_dni, p.nombre AS Paciente, t.Profesionales_idProfesionales, 
           pr.apellido AS Profesional, t.Especialidad_idEspecialidad, e.nombre AS Especialidad,
           f_hora, estado
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
    cursor.close()
    conexion.close()

def cambiar_estado_turno(dni, nuevo_estado):
    cursor, conexion = conectar()
    estados_permitidos = ["pendiente", "aceptado", "cancelado"]
    
    if nuevo_estado not in estados_permitidos:
        print("Estado no válido. Debe ser 'pendiente', 'aceptado' o 'cancelado'.")
        return

    cursor, conexion = conectar()
    try:
                sql = "UPDATE turno SET estado = %s WHERE Pacientes_dni = %s"
                values = (nuevo_estado, dni)
                cursor.execute(sql, values)
                conexion.commit()
                
                if cursor.rowcount > 0:
                    print(f"Estado del turno para el DNI {dni} cambiado a '{nuevo_estado}'.")
                else:
                    print(f"No se encontró un turno con el DNI {dni}.")
    except Error as e:
            print("Ocurrió un error al actualizar el estado:", e)
    finally:
            cursor.close()
            conexion.close()



def turnero():
    # Implementación de la función
    print("\n"*3)
    print("*"*6+" Turnero "+"*"*6)

    while True:
        print('Elija una de las siguientes opciones:')
        print('1. Crear Turno')
        print('2. Buscar Turno por DNI')
        print('3. Listado de Turnos por fecha')
        print('4. Actualizar Estado de Turno')
        print('5. Salir')
    
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
             print("\n")
             dni = input("Ingrese el DNI del paciente a actualizar el turno: ")
             nuevo_estado = input("¿A que estado quiere cambiar el Turno? (pendiente, aceptado, cancelado): ")
             cambiar_estado_turno(dni, nuevo_estado)

        elif option_pac == '5':
            print('SESIÓN TERMINADA')
            break
        else:
            print('OPCIÓN INVÁLIDA')
        

