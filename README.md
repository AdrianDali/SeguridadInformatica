Sistema de Cifrado y Descifrado con Autenticación JWT

Introducción

Este proyecto implementa un sistema de cifrado y descifrado de mensajes utilizando los algoritmos de César, Vigenère y Playfair. Además, el sistema cuenta con una API para el registro de usuarios y autenticación mediante JWT (JSON Web Tokens), con una funcionalidad de refresco del token para mantener sesiones seguras y manejables.

Este documento proporciona instrucciones sobre cómo descargar, instalar y ejecutar la API.

Requisitos Previos

Asegúrate de tener instalados los siguientes componentes:

Python 3.8+

Pip (gestor de paquetes para Python)

Virtualenv (opcional, pero recomendado)

Git (para clonar el repositorio)

Instrucciones de Instalación

Sigue estos pasos para instalar y configurar la API en tu entorno local.

Paso 1: Clonar el Repositorio

Primero, clona el repositorio del proyecto desde GitHub utilizando el siguiente comando:

$ git clone https://github.com/tu-usuario/tu-repositorio.git

Luego, navega al directorio del proyecto:

$ cd tu-repositorio

Paso 2: Crear un Entorno Virtual

Se recomienda utilizar un entorno virtual para evitar conflictos de dependencias. Puedes crear un entorno virtual con el siguiente comando:

$ python3 -m venv env

Activa el entorno virtual:

En Linux/macOS:

$ source env/bin/activate

En Windows:

$ .\env\Scripts\activate

Paso 3: Instalar Dependencias

Instala las dependencias requeridas usando pip:

$ pip install -r requirements.txt

Paso 4: Configurar Variables de Entorno

Crea un archivo .env en el directorio principal del proyecto para definir las variables de entorno necesarias. Por ejemplo:

SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=*

Estas variables se usan para la configuración de Django.

Paso 5: Migrar la Base de Datos

Realiza las migraciones necesarias para configurar la base de datos:

$ python manage.py migrate

Paso 6: Crear un Superusuario (Opcional)

Si deseas acceder al panel de administración de Django, crea un superusuario con el siguiente comando:

$ python manage.py createsuperuser

Paso 7: Ejecutar el Servidor

Inicia el servidor de desarrollo para ejecutar la API:

$ python manage.py runserver

Por defecto, la API estará disponible en http://localhost:8000/.

Endpoints Principales

Registro de Usuario: /api/register/ (POST)

Inicio de Sesión: /api/login/ (POST)

Refresco del Token: /api/token/refresh/ (POST)

Cifrado y Descifrado:

Cifrado César: /api/cifrado/cesar/ (POST)

Descifrado César: /api/descifrado/cesar/ (POST)

Cifrado Vigenère: /api/cifrado/vigenere/ (POST)

Descifrado Vigenère: /api/descifrado/vigenere/ (POST)

Cifrado Playfair: /api/cifrado/playfair/ (POST)

Descifrado Playfair: /api/descifrado/playfair/ (POST)

Cada solicitud a los endpoints de cifrado y descifrado requiere un token JWT válido en el encabezado de autorización:

Authorization: Bearer <token_de_acceso>

Pruebas y Uso

Puedes probar la API utilizando herramientas como Postman o cURL.

Ejemplo de Solicitud con cURL

Para registrar un usuario:

$ curl -X POST http://localhost:8000/api/register/ -H "Content-Type: application/json" -d '{"username": "usuario1", "password": "contraseñaSegura123"}'

Para obtener un token de acceso:

$ curl -X POST http://localhost:8000/api/login/ -H "Content-Type: application/json" -d '{"username": "usuario1", "password": "contraseñaSegura123"}'

Notas Adicionales

Asegúrate de mantener la SECRET_KEY segura y no compartirla públicamente.

En un entorno de producción, asegúrate de configurar DEBUG=False y utilizar un servidor web seguro.

Utiliza HTTPS para la comunicación entre el cliente y el servidor, especialmente cuando manejes información sensible.

Licencia

Este proyecto está bajo la licencia MIT.

Contacto

Si tienes alguna pregunta o necesitas ayuda, por favor contacta a [tu_email@example.com].

