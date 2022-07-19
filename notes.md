# Django Celery with RabbitMQ

## Message Broker

- Django - Tasks Messages - Message Broker
- Message broker include RabbitMQ and Redis
- Django - RabbitMQ - Celery(Which is a worker processer)
- Turn on the celery worker `celery -A src worker -l info` on windows we use the command `celery -A src worker -l info --pool=solo`
- Run the task on shell by just importing it `from app1.tasks import add` then `add.delay(1,4)` or `add.apply_async((2, 3))`

## Scheduling Tasks

### Working with flower

- `venv\lib\site\lib\site-packages\tornado\platform\asyncio.py`

#### Add this

- ```python3
  # asyncio.py script
  if sys.platform == 'win32':
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  ```

- Start Flower `flower -A src --port=5555` then navigate to port `http://127.0.0.1:5555`

- Install django_celery_beat which we can utilize to create periods

- To start celery beat `celery -A src beat -l INFO`

- To utilize the database scheduler we use the command `celery -A src beat -l INFO --scheduler django_celery_beat.schedulers.DatabaseScheduler`
