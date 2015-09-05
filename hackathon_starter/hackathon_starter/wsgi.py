"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/data/virt_env/django_starter/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/data/jobsearch/hackathon_starter')
sys.path.append('/data/jobsearch/hackathon_starter/hackathon')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon_starter.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/data/virt_env/django_starter/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
#
#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon_starter.settings")
#
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

