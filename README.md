# Gestión de Vehículos Django

Proyecto de un sitio web para la gestión y administración de vehículos con Django.

# Descripción

Permite a los usuarios observar y conocer las distintas características de los modelos de autos que se encuetren a la venta. 

Ofrece distintos filtros para observar una lista específica de autos en base a una característica que compartan (marca de auto, tipo de combustible, año de fabricación, etc).

Si el usuario tiene la sesión iniciada, puede agregar nuevos vehículos así como también modificar las características de un auto que ya se encuentre almacenado en la lista.

# Requerimientos

asgiref==3.8.1
certifi==2024.7.4
charset-normalizer==3.3.2
Django==5.0.6
idna==3.7
requests==2.32.3
sqlparse==0.5.0
typing_extensions==4.12.2
urllib3==2.2.2

# Instalación y configuración

1) Clonar el repositorio:

    ```sh
    git clone: git@github.com:LucianoAven/evaluacion-gestionVehiculos.git
    ```

2) Crear y activar un entorno virtual:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3) Instalar las dependencias necesarias para su funcionamiento:

    ```sh
    pip install -r requirements.txt
    ```

4) Crear y generar las migraciones:

    ```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5) Ejecutar el proyecto:

    ```sh
    python3 manage.py runserver
    ```

6) Acceder a la aplicación en tu navegador a través del siguiente enlace:

    ```
    http://127.0.0.1:8000/
     ```

# Funcionalidad de cada parte del proyecto

## Carpeta "home":

### Archivo "views.py:

Establece las funciones para que el usuario pueda iniciar o cerrar sesión. También vincula las funciones de las ventanas principales del sitio web (filtros e index) con sus archivos html.

### Archivo "urls.py":

Establece el enlace de internet donde se mostrarán las ventanas principales del proyecto.

### Archivos html de la carpeta "templates":

Diseña el frontend del proyecto donde los usuarios podrán visualizar las caracteristicas de los vehículos disponibles, la pantalla mostrará un mayor o menor número de funciones disponibles dependiendo si se encuetra la sesión iniciada.

## Carpeta "vehiculos":

### Archivo "models.py":

Genera las distintas bases de datos del proyecto más las columnas que contendrá cada una.

### Archivos de la carpeta "repositories":

Establece los disntintos comandos con funciones para filtrar, modificar o interactuar con las columnas de cada base de datos.

### Archivos de la carpeta "views":

Establece las vistas de cada base de datos que vinculan las funciones de los repositorios con los archivos html donde los usuarios podrán utilizar los distintos comandos para interactuar con las columnas de las bases de datos.

### Archivo "forms.py":

Establece los formularios que diseñarán los cuadros y barras de texto de las vistas donde los usuarios podrán ingresar o modificar información de las columnas.

### Archivo "urls.py":

Especifica cada enlace del sitio web donde se mostrará por pantalla cada ventana html del proyecto.

### Archivos de la carpeta "templates":

Generan el diseño de cada ventana del proyecto, como también el diseño de los distintos comandos que podrán realizar los usuarios, tanto los que se encuentren con la sesión iniciada como los que no. 

# Publicado por:

- Luciano Ciro Avendaño