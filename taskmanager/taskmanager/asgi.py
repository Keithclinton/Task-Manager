"""
ASGI config for taskmanager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

import sys
sys.path.append('C:/Windows/System32/task_manager_api/taskmanager')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

application = get_asgi_application()
