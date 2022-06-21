from .base import *


SECRET_KEY = 'django-insecure-8a88!l9*)=jzu4&3%b9bh$3t6lgdkow(4w4731ux!9q!f^mb1i'

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pointingdb',
        'USER':  'postgres',
        'PASSWORD': 'mugiwara',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}