"""
WSGI config for taskmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('C:/Windows/System32/task_manager_api/taskmanager')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

application = get_wsgi_application()
