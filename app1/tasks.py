from __future__ import absolute_import, unicode_literals # To ensure the celery module wont crash with the library

from celery import shared_task

@shared_task
def add(x, y):
    return x + y
# Turn on the celery worker - celery -A src worker -l info
# running the tasks on shell 