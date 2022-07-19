# Django Celery with RabbitMQ

## Message Broker

- Django - Tasks Messages - Message Broker
- Message broker include RabbitMQ and Redis
- Django - RabbitMQ - Celery(Which is a worker processer)
- Turn on the celery worker `celery -A src worker -l info`
- Run the task on shell by just importing it `from app1.tasks import add` then `add.delay(1,4)` or `add.apply_async((2, 3))`
