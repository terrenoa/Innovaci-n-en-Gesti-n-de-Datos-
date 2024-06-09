# Integrantes

    Nombre y apellido: Valentino Lorenzati
    Dni: 46508945
    Correo electronico: valentinolorenzati@gmail.com
    Link Github: https://github.com/VLorenzati
    Ejercicios: https://github.com/VLorenzati/solucionesPracticas

    Nombre y apellido: Alejo Nicolás Terreno
    Dni: 42783052    
    Correo electronico: anterreno12@gmail.com
    Link Github: https://github.com/terrenoa/
    Ejericios: https://github.com/terrenoa/evidencia2/

    Nombre y apellido: Emilio Masciarelli
    Dni: 33600010
    Correo electronico: emiliomasciarelli@gmail.com
    Link Github: https://github.com/EmiARG
    Ejercicios: https://github.com/EmiARG/solucionesPracticas

    Nombre y apellido: Gastón Di Campli
    Dni: 31055660
    Correo electronico: gaston.dicampli@gmail.com
    Link Github: https://github.com/Gdicampli22

    Nombre y apellido: Maria Lourdes Romero
    Dni: 46973418
    Correo electronico: lourdesromero843@gmail.com
    Link Github: https://github.com/luliromero

    Nombre y apellido: Lucila Natali Peire Moyano
    Dni: 39498736
    Correo electronico: lucipeire@gmail.com
    Link Github: https://github.com/Lucipeire

# Descripción del proyecto elegido:
El proyecto propuesto para esta instancia es el desarrollo de una aplicacion que facitile la gestión y administración de un hospital.
El objetivo es centralizar la información respecto a:
- Gestiones para Pacientes
  - alta/registro de paciente
  - modificación de paciente
  - baja de paciente
- Gestiones para Profesionales
  - alta/registro de paciente
  - modificación de paciente
  - baja de paciente
- Servicios médicos
  - consultar si un servicio es ofercido por el hospital
  - consultar la lista de todos los servicios ofrecidos
- Obras sociales
  - consultar si una obra social es recibida por el hospital
  - consultar la lista de todos las obras sociales recibidas
- Turnero
  - nuevo turno
  - consultar turnos
  - eliminar turno
  
En esta primera etapa lo que se plantea como solución es un una interfase que le permita al administrativo del hospital navegar entre las opciones que ofrece el programa.

### Datos de entrada:
El usuario la opción a la que quiere navegar ingresando un número entero.
### Datos de salida:
Listado de opciones que se muestra por pantalla
### Proceso:
El programa muestra una serie de opciones iniciales,
el usuario debe elegir una de las opciones ingresando uno de los números solicitados,
según sea la opción elegida el programa muestra una nueva lista de opciones específicas,
si no se elige una opción valida se muestra un mensaje de error y el proceso se reinicia.
### Variables:
- option: numero entero. Registra la opción elegida.
- option1: numero entero. Registra la opción especifica dentro de "gestiones para pacientes"
- option2: numero entero. Registra la opción especifica dentro de "gestiones para pprofesionales"
- option3: numero entero. Registra la opción especifica dentro de "servicios médicos"
- option4: numero entero. Registra la opción especifica dentro de "obras sociales"
- option5: numero entero. Registra la opción especifica dentro de "turnero"

### Diagrama de flujo
![hospital diagrama de flujo](https://github.com/EmiARG/ispcproyectointegrador/assets/85424039/949d243b-9ddf-4e4e-8126-782abd2d8fca)


### Detalle de la Aplicación Modularizada
Esta aplicación está diseñada siguiendo un enfoque modular, lo que significa que está dividida en varios archivos .py que cumplen funciones específicas . A continuación, se describe brevemente el propósito de cada archivo:

• index.py
Este archivo es el punto de entrada principal de la aplicación. Contiene la lógica principal de la aplicación y se encarga de coordinar la interacción entre los diferentes módulos.

• gestiones_para_pacientes.py
En este archivo se encuentran las funciones relacionadas con las gestiones de pacientes.  Va a manejar las operaciones de alta, modificación y baja de pacientes en la base de datos del hospital.

• gestiones_para_profesionales.py
En este archivos encontramos las  funciones relacionadas con las gestiones relacionadas con los profesionales. Gestiona las operaciones de alta, modificación y baja de profesionales médicos en la base de datos del hospital.

• obras_sociales.py
Este archivo contiene las funciones que van a relacionarse con la consulta de si una obra social es recibida por el hospital y obtener la lista de todas las obras sociales recibidas.

• servicios_medicos.py
En este archivo encontramos las funciones que van a estar relacionados con los tipos de servicios y especialidades ofrecidos por el hospital.

• turnero.py
Maneja las operaciones relacionadas con el turnero, como la creación de nuevos turnos, consulta de turnos y eliminación de turnos.
