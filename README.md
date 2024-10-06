# Integrantes

    Nombre y apellido: Valentino Lorenzati
    Dni: 46508945
    Correo electronico: valentinolorenzati@gmail.com
    Link Github: https://github.com/VLorenzati

    Nombre y apellido: Alejo Nicolás Terreno
    Dni: 42783052    
    Correo electronico: anterreno12@gmail.com
    Link Github: https://github.com/terrenoa/

    Nombre y apellido: Gastón Di Campli
    Dni: 31055660
    Correo electronico: gaston.dicampli@gmail.com
    Link Github: https://github.com/Gdicampli22

    
# Módulo Gestión e Innovacion de Datos

### Indice del repositorio

    ├── evidencia2/
    │   ├── BaseDeDatos/
    │   │   ├── script_bd.sql
    │   │   ├── DML.sql
    ├── evidencia1/
    │   ├── app/
    │   │   ├── aritmetica.py
    │   │   ├── captcha.py
    │   │   ├── logins.py
    │   │   ├── logs.txt
    │   │   ├── registrar.py
    │   │   ├── test_aritmetica.py
    │   │   ├── usuarios.txt
    │   │   └── validador_contraseñas.py
    │   ├── Informe.pdf
    ├── modulo programador 1° semestre...
    ├── README.md


En el archivo '''Informe.pdf''' describe el desarrollo de una aplicación de escritorio para la gestión 
y administración de un hospital. Este proyecto intenta dar solución a la necesidad de centralizar 
y simplificar la gestión de información en instituciones de salud, que manejan datos relacionados con pacientes, profesionales médicos, servicios, obras sociales y turnos. La aplicación busca proporcionar a los administrativos del hospital una herramienta 
eficiente, intuitiva y segura para realizar sus tareas diarias.

En cuanto a los módulos de la app:
- registrar.py: este módulo es el principal y funciona como INDEX de nuestra app. Integra los demás módulos, implementa las funciones de inicio de sesion y creación de nuevos usuarios. Se utulizo la libreria JSON para el manejo de archivos.
- aritmetica.py: según lo solicitado en la consigna, contiene funciones para las operaciones artiméticas básicas. Luego es utilizado en el módulo captcha.py.
- test_aritmetica.py: test del modulo anterior.
- captcha.py: para confirmar la creación del usuario solicita al usuario hacer la suma de dos valoreas aleatorios entre 0 y 10. Hace uso de la libreria random y del módulo aritmetica.py
- logins.py: haciendo uso de la libreria daytime se guardan cronologicamente los inicios de sesion en un archivo .txt
- validador_contraseñas.py: nuclea las operaciones de solicitud y validacion de calves según los requerimientos de la consigna. Utiliza la libreria re para el manejo de cadena de caracteres

*Mas detalle de la consigna de Base de Datos II, se encuentra escrito en Informe.pdf*
