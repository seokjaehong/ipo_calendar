from celery import shared_task


@shared_task
def say_hello():
    print('say_hello')


@shared_task
def test_task():
    print("hello world")
