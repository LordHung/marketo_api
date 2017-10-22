"""
WSGI config for marketo_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

loaded_env = "core.environments.development"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", loaded_env)

application = get_wsgi_application()
