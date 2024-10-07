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
    │   ├── Aplicacion/
    │   │   ├── acceso.py
    │   │   ├── accesos.ispc
    │   │   ├── gestion_accesos.py
    │   │   ├── gestion_usuarios.py
    │   │   ├── logs.txt
    │   │   ├── main.py
    │   │   ├── modelos.py
    │   │   ├── prueba.py
    │   │   ├── usuario.py
    │   │   ├── usuarios.ispc
    │   │   ├── utilidades.py
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

## Evidencia 2
### Descripción del proyecto

Este proyecto es una aplicación en Python que implementa un sistema de gestión de usuarios y accesos utilizando el paradigma de la Programación Orientada a Objetos (POO). La aplicación permite realizar un CRUD de usuarios (Crear, Leer, Actualizar y Eliminar) y gestionar los accesos de los mismos, registrando tanto los intentos exitosos como fallidos en archivos binarios y de texto. Los datos de los usuarios se almacenan en un archivo binario, y los accesos se registran en un archivo separado, mientras que los intentos fallidos se guardan en un log de texto.

### ¿Cómo ejecutar y probar este programa?

1. **Clonar el repositorio**:
   ```
   git clone [[URL del repositorio]](https://github.com/terrenoa/Innovaci-n-en-Gesti-n-de-Datos)

   ```

2. **Instalar dependencias**:
no es necesario instalar ninguna dependencia externa. Todos los requerimientos son nativos de python

3. **Ejecutar el programa**:
Para ejecutar el programa inicialice el archivo main.py

### Modulos
- acceso.py: se define la clase acceso y el metodo repr que permite devolver información sobre el loggeo.
- gestion_accesos.py: pide un usuario y contraseña. verifica que sea un usuario registrado y la contraseña sea correcta y registra en el archivo logs.txt si hay un intento fallido.
- gestion de usuarios.py: se definen las funciones que permiten hacer CRUD de usuarios.
- main.py: modulo principal, implementa los dos modulos anteriores.
- modelos.py: define las clases Usuario y Acceso, las cuales representan a los usuarios del sistema y los accesos de estos, respectivamente. Usuario es una clase que encapsula la información de un usuario del sistema. Acceso es una clase que registra los eventos de inicio de sesión de los usuarios en el sistema, permitiendo almacenar tanto el inicio como la salida del usuario
- usuario.py: deifne el metodo que permite obtener información de un usuario
- utilidades.py: administra los archivos usuarios.ispc y accesos.ispcc


<!-- Esto es un comentario vacío que genera espacio -->
<!-- Esto es un comentario vacío que genera espacio -->
<!-- Esto es un comentario vacío que genera espacio -->
<!-- Esto es un comentario vacío que genera espacio -->
### Evidencia 1
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
