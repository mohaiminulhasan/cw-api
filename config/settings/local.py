from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ['corsheaders', ]

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['*']
