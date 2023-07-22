import os
from celery import Celery

from girosmani.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'girosmani.settings')
app = Celery('girosmani', broker=CELERY_BROKER_URL, backend=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # can we indicate specific apps insted of all: lambda: settings.INSTALLED_APPS

