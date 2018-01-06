"""
WSGI config for marketo_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import WhiteNoise

ENV = "src.environments.development"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", ENV)

# application = get_wsgi_application()
application = WhiteNoise(get_wsgi_application())
