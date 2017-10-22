from src.settings import *
import os

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', '')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dev.marketo.com', ]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ['DB_PORT']
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Redis, store cache and sessions
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# STATIC_ROOT = os.path.join(BASE_DIR, '_static')
# STATICFILES_DIRS += [os.path.join(BASE_DIR, BACKUP_DIR_PATH), ]
