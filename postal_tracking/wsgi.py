"""
WSGI config for investments project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
# sys.path.append('/home/nginx/postal_tracking/postal_tracking')

# add the virtualenv site-packages path to the sys.path
# sys.path.append('/home/nginx/postal_tracking/lib/python3.4/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "postal_tracking.settings")

application = get_wsgi_application()
