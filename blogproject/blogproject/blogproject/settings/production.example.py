"""
Here be production settings
"""

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'example.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tag',
        'USER': 'tag',
        'PASSWORD': 'tag',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = 'S3cr3t K3y1'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'
