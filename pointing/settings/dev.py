from .base import *
from decouple import config

# SECRET_KEY = 'django-insecure-8a88!l9*)=jzu4&3%b9bh$3t6lgdkow(4w4731ux!9q!f^mb1i'

SECRET_KEY = config('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

# print(SECRET_KEY)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5432',
    }
}

# print(DATABASES)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [ 
    BASE_DIR / "static",
]