"""
WSGI config for Chizuterem_Ojinkeya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chizuterem_Ojinkeya.settings')

application = get_wsgi_application()
