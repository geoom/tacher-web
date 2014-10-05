
from .base import *

import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

INSTALLED_APPS += (
    'storages',
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


# Setup storage on S3 settings are stored as os.environs to keep settings.py clean
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
AWS_S3_SECURE_URLS = False  # use http instead of https
AWS_QUERYSTRING_AUTH = False  # dont add complex authentication-related query parameters for requests

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'https://s3-sa-east-1.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL
MEDIA_ROOT = ''
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'