"""
Development settings. This settings module extends from `settings.py`.

To enable this settings module instead of production, set the following environment variable:
    DJANGO_SETTINGS_MODULE="wolfizen_net.settings_dev"
"""
from wolfizen_net.settings import *

# Juicy debug information for the web server
DEBUG = True

# Serve pages to all hostnames
ALLOWED_HOSTS = []
