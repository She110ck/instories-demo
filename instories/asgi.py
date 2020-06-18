"""
ASGI config for instories project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instories.settings')

application = get_asgi_application()

# docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432  postgres