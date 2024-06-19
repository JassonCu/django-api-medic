
# Django rest framework - Vue Ts

Este proyecto consiste en el desarrollo de un sistema clínico moderno y escalable, diseñado para facilitar la gestión eficiente de datos médicos y la interacción fluida entre pacientes, médicos y personal administrativo.

Tecnologías Utilizadas:

    Backend: Django y Django REST Framework
        Django: Framework web de alto nivel que fomenta el desarrollo rápido y limpio, utilizando el patrón MVC (Modelo-Vista-Controlador).
        Django REST Framework: Potente conjunto de herramientas para construir APIs web utilizando Django, proporcionando serialización avanzada y vistas basadas en clases para crear APIs RESTful.

    Frontend: Vue.js
        Vue.js: Biblioteca progresiva para la construcción de interfaces de usuario, que facilita la creación de interfaces interactivas y reactivas mediante el uso de componentes reutilizables.
        Vuetify: Framework de componentes material design para Vue.js, utilizado para garantizar una interfaz de usuario consistente y atractiva.

Características del Sistema:

    Gestión de Pacientes: Permite registrar pacientes, actualizar su información personal y médica, así como gestionar sus citas y seguimientos.

    Historial Clínico Electrónico: Almacena de manera segura y organizada el historial médico completo de cada paciente, incluyendo diagnósticos, tratamientos previos, y resultados de exámenes.

    Agenda y Citas Médicas: Facilita la gestión de agendas médicas, permitiendo a los médicos programar citas, recibir notificaciones y gestionar disponibilidad de manera eficiente.

    Prescripción Electrónica: Permite a los médicos generar recetas electrónicas de forma segura y eficiente, integrando funcionalidades para la gestión de medicamentos y dosificaciones.

    Administración y Reportes: Incluye herramientas administrativas para la gestión de usuarios, roles y permisos, así como la generación de informes y estadísticas sobre la operación del centro médico.

Objetivos del Proyecto:

    Mejorar la eficiencia operativa del centro médico mediante la automatización de procesos.
    Optimizar la comunicación entre pacientes y personal médico.
    Cumplir con estándares de seguridad y privacidad de datos (como HIPAA, en el contexto estadounidense).
    Proporcionar una experiencia de usuario intuitiva y agradable a través de una interfaz moderna y responsive.

Beneficios Esperados:

    Reducción de errores en la gestión de datos médicos.
    Mejora en la precisión de diagnósticos y tratamientos.
    Incremento en la satisfacción tanto de pacientes como del personal médico.
    Adaptabilidad y escalabilidad para futuras expansiones y mejoras en el sistema.

Este proyecto integraría robustas tecnologías backend y frontend para proporcionar una solución completa y eficiente para la gestión de información médica y la atención al paciente en un entorno clínico moderno.


## Authors

- [@Jasson Rolando Cu](https://www.github.com/jassoncu)

---

## Instalación de forma local

Para instalar y ejecutar el proyecto localmente, sigue estos pasos:

#### 1. Clona el repositorio desde GitHub
```bash
git clone https://github.com/JassonCu/django-api-medic
```

#### 2. Accede al directorio del proyecto
```bash
cd django-api-medic
```

#### 3. Opcional: Crea un entorno virtual (recomendado)

Es una buena práctica utilizar un entorno virtual para manejar las dependencias del proyecto de forma aislada.

##### 3.1 En Windows
```bash
python -m venv venv
```

##### 3.2 En sistemas basados en Unix (Linux, macOS)
```bash
python3 -m venv venv
```

#### 4. Activa el entorno virtual (opcional pero recomendado)

Antes de instalar las dependencias del proyecto, activa el entorno virtual:

##### En Windows (cmd)
```bash
venv\Scripts\activate
```

##### En Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

##### En sistemas basados en Unix
```bash
source venv/bin/activate
```

#### 5. Instala las dependencias del proyecto

```bash
pip install -r requirements.txt
```

#### 6. Realiza las migraciones de la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Carga los datos de prueba (fixtures YAML)

Si tienes datos de prueba en formato YAML (fixtures) y deseas cargarlos en la base de datos, utiliza el comando `loaddata`:

```bash
python manage.py loaddata */fixtures/*.yaml
```

#### 8. Ejecuta el programa

Finalmente, con las migraciones aplicadas y los datos de prueba cargados, puedes ejecutar tu proyecto Django:

```bash
python manage.py runserver
```

------

## Variables de entorno necesarias

Para que el proyecto funcione correctamente, es necesario configurar algunas variables de entorno. Estas variables se utilizan principalmente para la configuración de la base de datos y la gestión de contenedores Docker. Puedes usar el archivo `.env-example` como referencia para crear tu propio archivo `.env`.

### Variables requeridas:

1. **Para la configuración de la base de datos MySQL:**
   - `MYSQLDB_HOST`: Host de la base de datos MySQL.
   - `MYSQLDB_PASSWORD`: Contraseña para el usuario de MySQL.
   - `MYSQLDB_ROOT_PASSWORD`: Contraseña del usuario root de MySQL.
   - `MYSQLDB_DATABASE`: Nombre de la base de datos que utilizará tu aplicación.
   - `MYSQLDB_LOCAL_PORT`: Puerto local utilizado para la conexión a MySQL desde fuera de Docker.
   - `MYSQLDB_DOCKER_PORT`: Puerto dentro del contenedor Docker donde MySQL está expuesto (generalmente 3306).

2. **Para la configuración de los contenedores Docker:**
   - `DJANGO_LOCAL_PORT`: Puerto local utilizado para acceder a tu aplicación Django desde fuera de Docker.
   - `DJANGO_DOCKER_PORT`: Puerto dentro del contenedor Docker donde se ejecutará tu aplicación Django.

### Consideraciones adicionales:

- Es recomendable tener instalado un gestor de base de datos MySQL. Si no lo tienes instalado localmente, puedes utilizar Docker para crear y gestionar un contenedor de MySQL de manera sencilla.
- Asegúrate de ajustar las variables de entorno según las especificaciones y configuraciones de tu entorno de desarrollo.

---

Para complementar la documentación con los comandos necesarios para crear una instancia de MySQL utilizando Docker, aquí tienes una sección adicional que puedes añadir:

---

## Creación de instancia de MySQL con Docker

Si no tienes MySQL instalado localmente o prefieres utilizar Docker para gestionar tu base de datos, puedes seguir estos pasos para crear una instancia de MySQL utilizando Docker.

#### 1. Descarga la imagen de MySQL desde Docker Hub

Ejecuta el siguiente comando para descargar la imagen oficial de MySQL desde Docker Hub:

```bash
docker pull mysql:latest
```

#### 2. Crea y ejecuta un contenedor MySQL

Utiliza el siguiente comando para crear y ejecutar un contenedor MySQL:

```bash
docker run -d --name mi-mysql \
    -e MYSQL_ROOT_PASSWORD=<root_password> \
    -e MYSQL_DATABASE=<database_name> \
    -p <local_port>:<docker_port> \
    mysql:latest
```

- Reemplaza `<root_password>` con la contraseña que deseas establecer para el usuario root de MySQL.
- Reemplaza `<database_name>` con el nombre que deseas asignar a tu base de datos.
- Reemplaza `<local_port>` con el puerto en tu máquina local que deseas mapear al contenedor de MySQL.
- Reemplaza `<docker_port>` con el puerto dentro del contenedor donde MySQL está expuesto (generalmente 3306).

#### Ejemplo:

```bash
docker run -d --name mi-mysql \
    -e MYSQL_ROOT_PASSWORD=mysecretpassword \
    -e MYSQL_DATABASE=mydatabase \
    -p 3306:3306 \
    mysql:latest
```

#### 3. Verifica que el contenedor MySQL esté en ejecución

Puedes verificar que el contenedor MySQL esté en ejecución utilizando el siguiente comando:

```bash
docker ps
```

Esto mostrará una lista de todos los contenedores Docker en ejecución. Deberías ver tu contenedor MySQL (`mi-mysql` en este ejemplo) listado.

#### 4. Conecta tu aplicación Django al contenedor MySQL

Utiliza las variables de entorno adecuadas (`MYSQLDB_HOST`, `MYSQLDB_PASSWORD`, etc.) en tu archivo `.env` para configurar la conexión de tu aplicación Django al contenedor MySQL que acabas de crear.

---

---

## Ejecución de pruebas (Tests)

Para verificar que todas las funcionalidades de tu aplicación están operando correctamente, puedes ejecutar los tests definidos en tu proyecto Django.

#### 1. Activa el entorno virtual (si no está activado)

Si aún no tienes activado tu entorno virtual, asegúrate de hacerlo para aislar las dependencias del proyecto:

##### En Windows (cmd)
```bash
venv\Scripts\activate
```

##### En Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

##### En sistemas basados en Unix
```bash
source venv/bin/activate
```

#### 2. Ejecuta los tests de Django

Utiliza el comando `manage.py` para ejecutar los tests definidos en tu aplicación Django:

```bash
python manage.py test
```

Este comando ejecutará todas las pruebas definidas en tu proyecto y mostrará los resultados en la consola.

#### Opciones adicionales:

- **Ejecutar tests de una aplicación específica:**
  Si deseas ejecutar tests solo para una aplicación específica en tu proyecto, puedes especificar el nombre de la aplicación después del comando `test`.

  ```bash
  python manage.py test <nombre_app>
  ```

- **Generar reporte HTML:**
  Para generar un reporte HTML de los resultados de los tests, puedes utilizar la opción `--html` seguido del nombre del archivo donde deseas guardar el reporte.

  ```bash
  python manage.py test --html=reporte_tests.html
  ```

#### 3. Verifica los resultados

Después de ejecutar los tests, verifica la salida en la consola para asegurarte de que todas las pruebas pasaron satisfactoriamente. Si algún test falla, revisa los detalles del error para identificar y corregir cualquier problema en tu código.

---
---

## Características del Proyecto

### Funcionalidades Principales:

1. **Autenticación de Usuarios:**
   - Registro de usuarios nuevos.
   - Inicio de sesión con autenticación segura.
   - Gestión de sesiones de usuario.

2. **Gestión de Datos:**
   - CRUD (Crear, Leer, Actualizar, Eliminar) para entidades principales del sistema.
   - Validación de datos y formularios.

3. **API RESTful:**
   - Exposición de endpoints RESTful para interactuar con datos.
   - Soporte para métodos HTTP (GET, POST, PUT, DELETE).

4. **Integración con Base de Datos:**
   - Conexión y gestión de base de datos MySQL.

5. **Seguridad:**
   - Implementación de medidas de seguridad como CSRF, CORS, y protección contra ataques XSS y SQL Injection.
   - Uso de tokens JWT para autenticación y autorización.

6. **Interfaz de Usuario (UI):**
   - Diseño responsive y accesible.
   - Implementación de componentes reutilizables.
   - Integración con librerías de diseño Vuefly.

7. **Pruebas Automatizadas:**
   - Suite de pruebas unitarias y de integración.
   - Cobertura de pruebas para todas las funcionalidades críticas.

8. **Internacionalización (i18n) y Localización (l10n):**
   - Soporte para múltiples idiomas y regiones.
   - Traducción de contenidos dinámicos y estáticos.

### Funcionalidades Adicionales:

1. **Gestión de Sesiones y Cookies:**
   - Mantenimiento de sesiones de usuario a través de cookies seguras.
   - Configuración de expiración de sesiones.

2. **Gestión de Archivos y Multimedia:**
   - Subida, almacenamiento y gestión de archivos (imágenes, documentos, etc.).

3. **Administración de Roles y Permisos:**
   - Definición de roles de usuario y permisos basados en roles.
   - Gestión de acceso y autorización a diferentes funcionalidades del sistema.

4. **Optimización de Rendimiento:**
   - Implementación de técnicas de optimización de carga y rendimiento (caching, compresión de recursos, etc.).

5. **Monitorización y Logging:**
   - Registro de eventos y errores para análisis y debugging.
   - Implementación de herramientas de monitorización para el rendimiento del sistema.

---

Muchas gracias, un abrazo. 🚀