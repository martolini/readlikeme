"""
Django settings for readlikeme project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@dhcw8duz5i)iq5n0fiqh32z7@8lcu05t!c))#+vlwk3nhpl#$'

# SECURITY WARNING: don't run with debug turned on in production!
PRODUCTION =  'floyd' in socket.gethostname()
DEBUG = True
THUMBNAIL_DEBUG = DEBUG

THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',

    'readlikeme.core',
    'readlikeme.core.profiles',

    'readlikeme.app',
    'readlikeme.app.reader',
    'readlikeme.app.viewcount',

    'pyjade',
    'readlikeme.external.django_ajax',
    'sorl.thumbnail',
    'paypal.standard.ipn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'readlikeme.urls'

WSGI_APPLICATION = 'readlikeme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if not PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'database.db'),
        }
    }
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'readlikeme',
            'USER': 'readuser',
            'PASSWORD': 'ReadThisPassword',
            'HOST': 'localhost',
            'PORT': '',                      # Set to empty string for default.
        }
    }
    MEDIA_ROOT = '/opt/readenv/media'
    STATIC_ROOT = '/opt/readenv/static'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "files/static"),
)

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'readlikeme/templates'),
)

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

LOGIN_URL = '/'

AUTH_USER_MODEL = 'profiles.Reader'
if PRODUCTION:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'unix:/opt/readenv/cache/memcached.sock',
        }
    }


# paypal
PAYPAL_RECEIVER_EMAIL = "buyer@flockwith.me"
PAYPAL_TEST = True