from pointing.settings import *
import dj_database_url

import cloudinary_storage



  
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']



ALLOWED_HOSTS = ['qr-pointing.herokuapp.com']

INSTALLED_APPS += [
	'cloudinary_storage',
]

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware",]
 
prod_db  =  dj_database_url.config()
DATABASES['default'].update(prod_db)

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dj8o7x845',
    'API_KEY': '466667418754698',
    'API_SECRET': 'kvnVj5GbhDC_XArBvXGHqtvUFCY'
}