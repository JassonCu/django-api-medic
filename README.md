# Django Rest Framework - Vue Ts

This project involves the development of a modern and scalable clinical system designed to facilitate efficient management of medical data and seamless interaction among patients, doctors, and administrative staff.

Technologies Used:

- Backend: Django and Django REST Framework
  - Django: High-level web framework that promotes rapid and clean development, using the MVC (Model-View-Controller) pattern.
  - Django REST Framework: Powerful toolkit for building web APIs using Django, providing advanced serialization and class-based views for creating RESTful APIs.

- Frontend: Vue.js
  - Vue.js: Progressive library for building user interfaces, making it easy to create interactive and reactive interfaces using reusable components.
  - Vuetify: Material Design component framework for Vue.js, used to ensure a consistent and appealing user interface.

System Features:

- Patient Management: Allows registering patients, updating their personal and medical information, as well as managing their appointments and follow-ups.

- Electronic Health Records: Safely and organized storage of each patient's complete medical history, including diagnoses, previous treatments, and test results.

- Scheduling and Medical Appointments: Facilitates medical schedule management, allowing doctors to schedule appointments, receive notifications, and manage availability efficiently.

- Electronic Prescriptions: Enables doctors to generate electronic prescriptions securely and efficiently, integrating functionalities for medication management and dosages.

- Administration and Reports: Includes administrative tools for user management, roles, and permissions, as well as generating reports and statistics on the medical center's operation.

Project Objectives:

- Improve the operational efficiency of the medical center through process automation.
- Optimize communication between patients and medical staff.
- Comply with data security and privacy standards (such as HIPAA in the US context).
- Provide an intuitive and pleasant user experience through a modern and responsive interface.

Expected Benefits:

- Reduction in errors in medical data management.
- Improved accuracy of diagnoses and treatments.
- Increased satisfaction of both patients and medical staff.
- Adaptability and scalability for future system expansions and improvements.

This project integrates robust backend and frontend technologies to provide a comprehensive and efficient solution for medical information management and patient care in a modern clinical environment.

## Authors

- [@Jasson Rolando Cu](https://www.github.com/jassoncu)

---

## Local Installation

To install and run the project locally, follow these steps:

#### 1. Clone the repository from GitHub
```bash
git clone https://github.com/JassonCu/django-api-medic
```

#### 2. Navigate to the project directory
```bash
cd django-api-medic
```

#### 3. Optional: Create a virtual environment (recommended)

It's a good practice to use a virtual environment to manage project dependencies in isolation.

##### 3.1 On Windows
```bash
python -m venv venv
```

##### 3.2 On Unix-based systems (Linux, macOS)
```bash
python3 -m venv venv
```

#### 4. Activate the virtual environment (optional but recommended)

Before installing project dependencies, activate the virtual environment:

##### On Windows (cmd)
```bash
venv\Scripts\activate
```

##### On Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

##### On Unix-based systems
```bash
source venv/bin/activate
```

#### 5. Install project dependencies

```bash
pip install -r requirements.txt
```

#### 6. Perform database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Load test data (YAML fixtures)

If you have test data in YAML format (fixtures) and want to load it into the database, use the `loaddata` command:

```bash
python manage.py loaddata */fixtures/*.yaml
```

#### 8. Run the application

Finally, with migrations applied and test data loaded, you can run your Django project:

```bash
python manage.py runserver
```

---

## Required Environment Variables

To ensure the project runs correctly, configure the following environment variables. These variables are primarily used for MySQL database configuration and Docker container management. You can use the `.env-example` file as a reference to create your own `.env` file.

### Required Variables:

1. **For MySQL database configuration:**
   - `MYSQLDB_HOST`: MySQL database host.
   - `MYSQLDB_PASSWORD`: Password for the MySQL user.
   - `MYSQLDB_ROOT_PASSWORD`: Password for the MySQL root user.
   - `MYSQLDB_DATABASE`: Name of the database your application will use.
   - `MYSQLDB_LOCAL_PORT`: Local port used to connect to MySQL from outside Docker.
   - `MYSQLDB_DOCKER_PORT`: Port inside the Docker container where MySQL is exposed (usually 3306).

2. **For Docker container configuration:**
   - `DJANGO_LOCAL_PORT`: Local port used to access your Django application from outside Docker.
   - `DJANGO_DOCKER_PORT`: Port inside the Docker container where your Django application will run.

### Additional Considerations:

- It is recommended to have MySQL database management system installed. If not installed locally, you can use Docker to easily create and manage a MySQL container.
- Make sure to adjust the environment variables according to your development environment specifications and configurations.

---

To complement the documentation with the necessary commands for creating a MySQL instance using Docker, here's an additional section you can add:

---

## Creating MySQL Instance with Docker

If you do not have MySQL installed locally or prefer to use Docker to manage your database, follow these steps to create a MySQL instance using Docker.

#### 1. Pull MySQL image from Docker Hub

Run the following command to download the official MySQL image from Docker Hub:

```bash
docker pull mysql:latest
```

#### 2. Create and run a MySQL container

Use the following command to create and run a MySQL container:

```bash
docker run -d --name my-mysql \
    -e MYSQL_ROOT_PASSWORD=<root_password> \
    -e MYSQL_DATABASE=<database_name> \
    -p <local_port>:<docker_port> \
    mysql:latest
```

- Replace `<root_password>` with the password you want to set for the MySQL root user.
- Replace `<database_name>` with the name you want to assign to your database.
- Replace `<local_port>` with the port on your local machine you want to map to the MySQL container.
- Replace `<docker_port>` with the port inside the container where MySQL is exposed (usually 3306).

#### Example:

```bash
docker run -d --name my-mysql \
    -e MYSQL_ROOT_PASSWORD=mysecretpassword \
    -e MYSQL_DATABASE=mydatabase \
    -p 3306:3306 \
    mysql:latest
```

#### 3. Verify MySQL container is running

You can verify that the MySQL container is running by using the following command:

```bash
docker ps
```

This will display a list of all running Docker containers. You should see your MySQL container (`my-mysql` in this example) listed.

#### 4. Connect your Django application to MySQL container

Use the appropriate environment variables (`MYSQLDB_HOST`, `MYSQLDB_PASSWORD`, etc.) in your `.env` file to configure your Django application's connection to the MySQL container you just created.

---

## Running Tests

To verify that all functionalities of your application are working correctly, you can run the tests defined in your Django project.

#### 1. Activate the virtual environment (if not activated)

If you haven't already activated your virtual environment, make sure to do so to isolate the project dependencies:

##### On Windows (cmd)
```bash
venv\Scripts\activate
```

##### On Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

##### On Unix-based systems
```bash
source venv/bin/activate
```

#### 2. Run Django tests

Use the `manage.py` command to run the tests defined in your Django application:

```bash
python manage.py test
```

This command will execute all tests defined in your project and display the results in the console.

#### Additional options:

- **Run tests for a specific application:**
  If you want to run tests only for a specific application in your project, you can specify the application name after the `test` command.

  ```bash
  python manage.py test <app_name>
  ```

- **Generate HTML report:**
  To generate an HTML report of the test results, you can use the `--html` option followed by the filename where you want to save the report.

  ```bash
  python manage.py test --html=test_report.html
  ```

#### 3. Verify the results

After running the tests, check the console output to ensure that all tests passed successfully. If any test fails, review the error details to identify and correct any issues in your code.

---

---

## Project Features

### Core Features:

1. **User Authentication:**
   - New user registration.
   - Secure login authentication.
   - User session management.

2. **Data Management:**
   - CRUD (Create, Read, Update, Delete) for core system entities.
   - Data validation and form handling.

3. **RESTful API:**
   - Exposing RESTful endpoints to interact with data.
   - Support for HTTP methods (GET, POST, PUT, DELETE).

4. **Database Integration:**
   - Connection and management of MySQL database.

5. **Security:**
   - Implementation of security measures such as CSRF, CORS, and protection against XSS and SQL Injection.
   - Use of JWT tokens for authentication and authorization.

6. **User Interface (UI):**
   - Responsive and accessible design.
   - Implementation of reusable Vuefly design components.

7. **Automated Testing:**
   - Suite of unit and integration tests.
   - Test coverage for all critical

 functionalities.

8. **Internationalization (i18n) and Localization (l10n):**
   - Support for multiple languages and regions.
   - Translation of dynamic and static content.

### Additional Features:

1. **Session and Cookie Management:**
   - Maintenance of user sessions through secure cookies.
   - Session expiration configuration.

2. **File and Media Management:**
   - Upload, storage, and management of files (images, documents, etc.).

3. **Role and Permission Management:**
   - User role definition and permissions based access.
   - Management of access and authorization to different system functionalities.

4. **Performance Optimization:**
   - Implementation of load and performance optimization techniques (caching, resource compression, etc.).

5. **Monitoring and Logging:**
   - Logging of events and errors for analysis and debugging.
   - Implementation of monitoring tools for system performance.

---

Thank you very much, and best regards. 🚀