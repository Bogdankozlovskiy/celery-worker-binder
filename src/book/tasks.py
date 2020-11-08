from celery import shared_task
from book.models import Holiday


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def hello():
	quary_length = Holiday.objects.all().count()
	return f"hello world {quary_length}"
