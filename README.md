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

    Nombre y apellido: Gastón Di Campli
    Dni: 31055660
    Correo electronico: gaston.dicampli@gmail.com
    Link Github: https://github.com/Gdicampli22
# Módulo Gestión e Innovacion de Datos

El presente informe describe el desarrollo de una aplicación de escritorio para la gestión 
y administración de un hospital. Este proyecto intenta dar solución a la necesidad de centralizar 
y simplificar la gestión de información en instituciones de salud, que manejan grandes 
volúmenes de datos relacionados con pacientes, profesionales médicos, servicios, obras sociales 
y turnos. La aplicación busca proporcionar a los administrativos del hospital una herramienta 
eficiente, intuitiva y segura para realizar sus tareas diarias.
La solución propuesta será desarrollada en el lenguaje de programación Python, 
utilizando una base de datos relacional gestionada por MySQL. Este proyecto pretende dar 
continuidad al desarrollo propuesto para el trabajo final del módulo programador del primer 
semestre de la carrera.
En línea con los objetivos de la cátedra, con el avance del proyecto se implementará el 
uso de librerías específicas de Python tales como Pandas, Numpy y Matplotlib. Asimismo, se 
implementará el paradigma de Programación Orientada a Objetos (POO), lo cual permitirá una 
estructuración más clara y mantenible del código, facilitando su escalabilidad en el futuro.






# módulo programador 1° semestre 2024
## Descripción del proyecto elegido y analisis EPS
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


# Modularización y guia del repositorio
Esta aplicación está diseñada siguiendo un enfoque modular, lo que significa que está dividida en varios archivosque cumplen funciones específicas. Loss archivos se encuentran organizados en carpetas para facilitar su identificación y mantener los archivos ordenados y prolijos.
### Carpeta aplicacion
Esta carpeta contiene los archivos .py donde se encuentran distribuidas las funciones e implementaciónes que componen nuestra aplicación.
A continuación, se describe brevemente el propósito de cada archivo:

- index.py
Este archivo es el punto de entrada principal de la aplicación. Contiene la lógica principal de la aplicación y se encarga de coordinar la interacción entre los diferentes módulos.

- gestiones_para_pacientes.py
En este archivo se encuentran las funciones relacionadas con las gestiones de pacientes.  Va a manejar las operaciones de alta, modificación y baja de pacientes en la base de datos del hospital.

- gestiones_para_profesionales.py
En este archivos encontramos las  funciones relacionadas con las gestiones relacionadas con los profesionales. Gestiona las operaciones de alta, modificación y baja de profesionales médicos en la base de datos del hospital.

- obras_sociales.py
Este archivo contiene las funciones que van a relacionarse con la consulta de si una obra social es recibida por el hospital y obtener la lista de todas las obras sociales recibidas.

- especialidad.py
En este archivo se defienen las funciones de alta, modificacion y baja ademas de su implementación para las especialidades que que ofrece el hospital.

- obras_especialidad.py
En el archivo se encuentran las funciones que permiten identificar que especialidad medica es cubierta por cada obra social.

- profesionales_especialidad.py
En el archivo se encuentran las funciones que permiten vincular a los profesionales con la especialidad que atienden en el hospital.

- turnero.py
Este es el archivo mas complejo e importante del programa, a partir de todos los anteriores genera la informacion necesaria para agendar un turno, ademas de consultar y eliminar turnos.

- servicios_medicos.py
Este archivo fomraba parte de la concepcion original del proyecto pero con la evolucion decidimos posponer su implementación y reemplazarlo por el archivo especialidad.py que se ajustaba mejor a las caracteristicas de la consigna. Sin embargo preferimos no eliminarlo con la intencion de que en una futura actualización pueda ser una caracteristica que le de valor agregado al programa.

### Carpeta base de datos
- diagrama entidad realcion.pdf
DER de la primera concepcion de la base de datos diseñada para el proyecto

- diagramacrowfoot.mwb
Contiene el diagrama crow foot de la base de datos utilizada en la implementación final, acusa la evolución en la concepcion del proyecto y los cambios implementados para lograr una mejor resolucion de la situacion problematica.

- diagramaCrowFoot.mwb.bak
backup del anterior

- diagramaCrowFoot.PNG
idem que los anteriores pero en formato de imagen

- script_bd.sql
Archivo que contiene el esquema de la base de datos utilizada en el programa.

- DML.sql
Este archivo contiene todas las consultas realizadas a la base de datos para poder lograr las funciones implementadas en la el programa.

### Carpeta dump_datos

Contiene los archivos script de los datos alojados en la database, datos ficticios insertados en la base de datos para probar su funcionamiento

### Carpeta prueba
En esta carpeta se encuentran archivos que fueron utilizados para hacer pruebas y experimentar con las herramientas disponibles para lograr la materialización del proyecto, pero no agregan funcionalidad alguna.

# Requisitos y puesta en marcha.
Antes de iniciar el programa es necesario tener instalado python, la libreria de python mysql.connector; y mysql.
Esta aplicación no cuenta con una interfaz gráfica por lo que debe ser ejecutada desde consola.
## Paso a paso
1. Instale las dependencias requeridas.
2. Clone el repositorio en un repositorio local
3. Haciendo uso de los archivos .sql importer la base de datos en mysql workbench
4. Desde mySQL Workbench genere una nueva conexión
5. Edite el codigo fuente con sus credenciales de conexión con la base de datos.
6. Inicialice el archivo index.py

