"""
Django settings for myhvacrguide project.

Development mode
"""

from .base import *


###############################################################################
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.0.36',
    '192.168.0.35',
    '192.168.123.1',
    ]

INTERNAL_IPS = [
    '127.0.0.1',
    '192.168.0.36',
    '192.168.0.35',
    '192.168.123.1',
]


###############################################################################
# Application definition

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


###############################################################################
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


###############################################################################
# Email
# https://docs.djangoproject.com/fr/2.2/topics/email/

# > Email dans la console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


###############################################################################
# Django-recaptcha
# https://pypi.org/project/django-recaptcha/

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


###############################################################################
# SCSS
COMPRESS_OFFLINE = True
COMPRESS_ENABLED = False
