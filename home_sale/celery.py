from __future__ import absolute_import
import os

from celery import Celery
from home_sale.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home_sale.settings.development")

app = Celery("home_sale")

app.config_from_object("home_sale.settings.development")

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)