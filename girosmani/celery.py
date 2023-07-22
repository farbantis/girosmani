import os
from celery import Celery

from girosmani.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'girosmani.settings')
app = Celery('girosmani')
app.config_from_object('django.conf:settings', namespace='CELERY')  # from settings will load backend
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks()  # can we indicate specific apps insted of all: lambda: settings.INSTALLED_APPS

