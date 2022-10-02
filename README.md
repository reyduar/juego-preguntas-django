# 🚀 Juego de preguntados sobre la provincia del Chaco

## Demo

https://juegochacoapp.herokuapp.com/login

## Configuración del entorno de desarrollo

- Instalar [Visual Studio Code](https://code.visualstudio.com/download) como IDE.

### Extensiones Requeridas en VS Code

- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [Python](https://github.com/Microsoft/vscode-python)

### Instalaciones obligatorias

- [Python 3.9](https://www.python.org/downloads/)

### Instalaciones de paquetes necesarios con pip de forma local

La configuracion de un entorno virtual queda a cargo de cada developer como quiera trabajar, las librerias necesarias que necesita tener instalado en su entorno local estan en el archvivo `requirements.txt` y se puede instalar directamente con este comando:

```
pip install -r requirements.txt
```

### [DEPRECADO] Pasos para configurar y corre el proyecto localmente en un entorno virtual

> Importante: Tenes Git instalado y configurado localmente con una public key SSH. Todos estos pasos se realizaran por linea de comandos.

En el repositorio se subio el archivo `Pipfile` que es la configuración del entorno virtual que estamos utilizando, por lo tanto lo unico que necesitamos hacer es:

1. Abrimos una consola (CMD), vamos a la unidad `C:/`.

2. Clonamos el proyecto con `git clone git@github.com:javierduartepy/proyecto-final-django.git`, esto nos crea un carpeta llamada `proyecto-final-django` con todo el contenido del proyecto.

3. Vamos por consola dentro de la carpeta del proyecto `cd proyecto-final-django` y corremos el siguiente comando `pipenv install`, esto crea el entorno virtual.

4. Activamos el entorno virtual con `pipenv shell`, este paso es necesario para ejecutar el proyecto de forma local.

5. Para ejecutar el proyecto de forma local entramos a la carpteta `cd QuizChacoApp` y ejecutamos el comando `python manage.py runserver`

> Nota: Si el pipenv no funciona se pueden instalar los paquetes de proyecto ejecutando el comando "pip install -r requirements.txt" dentro de la carpeta "QuizChacoApp"

6. En el navegador pegamos la url -> `http://127.0.0.1:8000/` y nos muestra la vista de Home

### Pasos para el despliegue en Heroku

1. Instalación de gunicorn

Paquete para los comandos en el servidor de heroku

```
pip install gunicorn
```

2. Instalación de psycopg2

Paquete para la base de datos PostgresSQL

```
pip install psycopg2-binary
pip install psycopg2
```

3. Instalamos la librería dj-database-url

Para la base datos externa al proyecto que vamos a utilizar

```
pip install dj-database-url
```

4. Instalamos la librería de python-decouple
   Para la lectura de variables de entornos

```
pip install python-decouple
```

5. Instalamos whitenoise

Sirve para archivos estáticos en prod

```
pip install whitenoise
```

6. Instalamos django-heroku

```
pip install django-heroku
```

7. Instalamos python-dotenv

Esta libreria nos permite crear un entorno local para nuesta base de datos, para poder usar sqlite3 localmente y postgresql en heroku

```
pip install python-dotenv
```

8. Creamos el archivo requirements.txt

```
pip freeze > requirements.txt
```

9. Así quedaría nuestro Settings.py al finalizar la configuración

```ts
import dj_database_url
import os
from pathlib import Path
import dj_database_url
from decouple import config
import dotenv
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Este codigo hace que se lea de forma local el archivo .env para usar SQLite3
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ii4gmfj8k1a!@3sf*x7jgoqi(u_x!&3o09r-%(da*9_6(8s0%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # Se modifico esta linea


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'juego'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware' # Se agrego esta linea
]

ROOT_URLCONF = 'QuizChacoApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'QuizChacoApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Con esta configuracion tomamos de forma local SQLite3 y en Heroku PostgreSQL
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Se agrego esta linea
STATIC_URL = '/static/'

STATIC_DIRS = (os.path.join(BASE_DIR, 'static'),) # Se agrego esta linea

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Se agrego esta linea
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Activate Django-Heroku.
django_heroku.settings(locals()) # Se agrego esta linea
del DATABASES['default']['OPTIONS']['sslmode'] # Se agrego esta linea

```

10. Creamos un archivo .env para simular en el entorno local la variable DATABASE_URL

Creamos en el directorio raiz un archivo llamado `.env` y dentro le agregamos el siguiente valor:

```
DATABASE_URL=sqlite:///db.sqlite3
```

11. Modificamos el archivo urls.py

```ts
# importamos estas librerias
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', core_views.inicio, name='inicio'),
    path('inicio/', core_views.inicio, name='inicio'),
    path('acercade/', core_views.acercade, name='acercade'),
    path('juego/', juego_views.juego, name='juego'),
    path('ayuda/', core_views.ayuda, name='ayuda'),
    path('miscelanea/', core_views.miscelanea, name='miscelanea'),
    path('categoria/', juego_views.categoria, name='categoria'),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # se agrego esta parte + static...
```

12. Creamos la carpeta `static` en el directorio raíz donde está el archivo manage.py

Dentro de esta carpeta creamos un archivo vacío llamado `.keep`

13. Creamos el archivo `Procfile` en el directorio raiz donde estaba el archivo manage.py

Agregamos el siguiente valor

```
web: gunicorn QuizChacoApp.wsgi --log-file -
```

14. Instalamos Heroku CLI

- https://devcenter.heroku.com/articles/heroku-cli
- [Descargar Heroku para Win64](https://cli-assets.heroku.com/heroku-x64.exe)

15. Iniciamos sesión en Heroku por consola

```
heroku login
```

16. Creamos un proyecto en Heroku con heroku cli (Esto se hace solo la primera vez)

```
heroku create juegochacoapp
```

17. En el directorio raíz del proyecto donde está él .git indexamos nuestro repositorio con heroku (Esto se hace solo la primera vez)

```
heroku git:remote -a juegochacoapp
```

18. Agregamos el addons para la base de datos (Esto se hace solo la primera vez)

```
heroku addons:create heroku-postgresql:hobby-dev
```

Created postgresql-slippery-31315 as DATABASE_URL

19. Subimos nuestro proyecto al repo de heroku

Este proceso tarda un poco,

```
git push heroku master
```

En el caso que necesitemos subir alguna actualización y volver a desplegar la app, estos son los pasos:

```
$ heroku login
$ cd [a la carpeta raiz el proyecto]
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

20. Ejecutar las migraciones del proyecto en la base de datos

```
heroku run python manage.py migrate

```

Posiblemente si no encuentra el favicon, vamos a correr este comando en Heroku

```
heroku run python manage.py collectstatic
```

21. Podemos ir heroku entramos a nuestro proyecto -> settings para encontrar la url

Url de las apps en Heroku

- https://dashboard.heroku.com/apps
  Url del proyecto
- https://dashboard.heroku.com/apps/quizchacoapp
  Url de la aplicacion desplegada
- https://quizchacoapp.herokuapp.com/

También podemos ejecutar nuestra url usando el siguiente comando

```
heroku open
```

22. Pasos para crear un superuser en Heroku (Es necesario hacerlo una unica vez)

```
heroku run python manage.py createsuperuser
```

```js
username: superusuarioadmin
email: dante2021@gmail.com
password: dante2021
```

- URL del Juego

https://juegochacoapp.herokuapp.com/

- URL para entrar al Admin de Django en Heroku

https://juegochacoapp.herokuapp.com/admin/

### DER

![DER](https://i.postimg.cc/SQc2203h/der.jpg)
