"""
LOCAL ES PARA CUANDO TRABAJAMOS DE FORMA LOCAL
QUITAR:
    - Todo lo que estaba en base.py y dejando todo eso que se quito del mismo para luego importarlo
DEJAR: 
    - Security Warning --> debug, allowed_hosts
    - Databases
    - Static Url

Para correrlo hay que activar el entorno virtual y luego correr el servidor con la nueva ruta de settings.py
python manage.py runserver --settings=empleado.settings.local
Esto permite correr el programa desde LOCAL.PY, --settings aclara que queremos trabajar con esa carpeta, que se encuentra 
dentro de empleado, dentro de la carpeta settings(creada) y elegir el archivo con cual queremos iniciar(en este caso local.py)


"""

# IMPORTAR BASE
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # carpeta base static

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' 

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
