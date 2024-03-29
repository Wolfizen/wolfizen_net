"""
Production settings for wolfizen.net.
This file is the default, and will be used if no other steps are taken.
This default is specified in `manage.py`.
"""
import os
import sys

from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: os.path.join(base_dir, ...)
here_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(here_dir)


# Security

# The secret key is stored in a separate file, not in source control.
# The key is auto-generated on first run.
try:
    from wolfizen_net.secret_key import SECRET_KEY
except ImportError:
    print("Secret key file is empty... generating and saving to 'secret_key.py'.")
    secret_key_file = open(os.path.join(here_dir, "secret_key.py"), "w")
    secret_key_file.write(f'SECRET_KEY = "{get_random_secret_key()}"\n')
    secret_key_file.close()
    # noinspection PyUnresolvedReferences
    try:
        from wolfizen_net.secret_key import SECRET_KEY
    except ImportError:
        print("Secret key file still empty after generating it.. skipping.")

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'wolfizen.net']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'wolfizen_net.apps.main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wolfizen_net.urls'
APPEND_SLASH = False

WSGI_APPLICATION = 'wolfizen_net.wsgi.application'

TEMPLATE_DIR = os.path.join(base_dir, os.path.join('wolfizen_net', 'templates'))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

# CachedViewMixin default max-age.
CACHE_CONTROL_DEFAULT_MAX_AGE = 86400


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(base_dir, 'db.sqlite3'),
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(base_dir, 'static')
STATICFILES_DIRS = [os.path.join(base_dir, os.path.join('wolfizen_net', 'assets'))]


# Dynamic files (uploaded images, generated files)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(base_dir, 'media')


# Logging

# https://stackoverflow.com/questions/42122815/how-to-configure-django-logging-for-production-under-gunicorn-server
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'gunicorn.errors': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        }
    }
}
