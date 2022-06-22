from .base import *
from decouple import config

SECRET_KEY = 'django-insecure-8a88!l9*)=jzu4&3%b9bh$3t6lgdkow(4w4731ux!9q!f^mb1i'
DEBUG = False
ALLOWED_HOSTS = ['51.75.123.207']

CORS_ALLOWED_ORIGINS = [
    'http://51.75.123.207',
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pointing_db',
        'USER': 'hakeem',
        'PASSWORD': 'mugiwara',
        'HOST': 'localhost',
        'PORT': '',
    }
} 