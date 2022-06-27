from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['51.75.123.207']

# CORS_ALLOWED_ORIGINS = [
# 	'http://51.75.123.207',
# ]

CORS_ALLOW_ALL_ORIGINS = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}