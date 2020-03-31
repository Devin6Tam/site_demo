"""
WSGI config for site_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/

WSGI (Web Server Gateway Interface)
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_demo.settings')

application = get_wsgi_application()

sys.path.append("/python/web_station/site_demo")