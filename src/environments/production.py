from src.settings import *
import os

DEBUG = True

# SECRET_KEY = os.environ.get('SECRET_KEY', '5y1ytgnq%*!&#qky0w%1eo)n9xluno3@6m!)su+%2mm0==isuo')
SECRET_KEY = '5y1ytgnq%*!&#qky0w%1eo)n9xluno3@6m!)su+%2mm0==isuo'

ALLOWED_HOSTS = ['https://marketo-django.herokuapp.com', ]

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
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://redis:6379/0',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'
