from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj.settings')

app = Celery('proj')

app.conf.enable_utc = False

app.conf.update(timezone = "Asia/Kolkata")

app.config_from_object(settings,namespace = 'CELERY')

app.conf.beat_schedule = {
    "send-mail-every-day-at-8":{
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour = 0 ,minute=10),
        # 'args': (2,)
    }
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request:{self.request}")