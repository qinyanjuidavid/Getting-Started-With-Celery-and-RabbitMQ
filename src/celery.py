# from  __future__ import absolute_import, unicode_literals #To ensure the celery module wont crash with the library

# import os

# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
# app = Celery('src') # Create a new Celery instance, src is the project name

# app.config_from_object('django.conf:settings', namespace='CELERY') # Load the settings from the django settings file
# app.autodiscover_tasks() # Load the tasks from the tasks.py file in the applications


from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))