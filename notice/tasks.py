from celery import shared_task


@shared_task
def say_hello():
    print('say_hello')


@shared_task
def test_task():
    print("hello world")

@shared_task()
def daily_check():
    from notice.telegram import job
    job()