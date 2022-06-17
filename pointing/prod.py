from pointing.settings import *
import dj_database_url






DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = 'DNt;*d7X4"MZ#;#%;YJEiApKs/[(TJ4l#>XYv$2G@n>7AkoROLYLXW)^=CaQ;a]'

ALLOWED_HOSTS = ['qr-pointing.herokuapp.com']

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware",]
 
prod_db  =  dj_database_url.config()
DATABASES['default'].update(prod_db)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"