"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# 1) Add your project path
project_path = '/home/HariniM/Portfolio'
if project_path not in sys.path:
    sys.path.append(project_path)

# 2) Point to your Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

# 3) WSGI app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
