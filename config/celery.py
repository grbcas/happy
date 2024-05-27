from __future__ import absolute_import
import os
from celery import Celery
import time
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'task_notify-everyday': {
        'task': 'tasks.task_notify',
        'schedule': crontab(),
    },
}

app.conf.timezone = 'UTC'


@app.task()
def debug_task():
    print(f'running.....debug_task')
    time.sleep(5)
