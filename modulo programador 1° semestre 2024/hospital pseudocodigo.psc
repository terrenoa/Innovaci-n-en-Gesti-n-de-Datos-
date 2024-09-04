Algoritmo hospital
	Mientras Verdadero Hacer
		Escribir '******HOSPITAL HOSPITAL******'
		Escribir 'Bienvenido al programa de gestion hospitalaria'
		Escribir ' Elija una de las siguientes opciones: '
		Escribir '1. Gestiones para pacientes'
		Escribir '2. Gestiones para profesionales'
		Escribir '3. Servicios médicos'
		Escribir '4. Obras sociales'
		Escribir '5. Turnero'
		Escribir '6. Salir'
		Leer option
		Si option=1 Entonces
			Escribir 'GESTIONES PARA PACIENTES'
			Escribir ' Elija una de las siguientes opciones: '
			Escribir '1. Alta pacientes'
			Escribir '2. Modificación pacientes'
			Escribir '3. Consulta pacientes'
			Leer option1
		SiNo
			Si option=2 Entonces
				Escribir 'GESTIONES PARA PROFESIONALES'
				Escribir ' Elija una de las siguientes opciones: '
				Escribir '1. Alta profesional'
				Escribir '2. Modificación profesionales'
				Escribir '3. Consulta profesionales'
				Leer option2
			SiNo
				Si option=3 Entonces
					Escribir 'SERVICIOS MEDICOS'
					Escribir 'Elija una de las siguientes opciones'
					Escribir '1. Consultar servicio'
					Escribir '2. Consultar listado'
					Leer option3
				SiNo
					Si option=4 Entonces
						Escribir 'OBRAS SOCIALES'
						Escribir 'Elija una de las siguientes opciones'
						Escribir '1. Consultar obra social'
						Escribir '2. Consultar listado'
						Leer option4
					SiNo
						Si option=5 Entonces
							Escribir 'TURNERO'
							Escribir '1. Nuevo turno'
							Escribir '2. Consultar turnos'
							Escribir '3. Eliminar turno'
							Leer option5
						SiNo
							Si option=6 Entonces
								Escribir 'SESIÓN TERMINADA'
							SiNo
								Escribir 'OPCIÓN INVÁLIDA'
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinMientras
FinAlgoritmo
