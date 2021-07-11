import os

import django
from celery import Celery

# `celery` 프로그램을 작동시키기 위한 기본 장고 세팅 값을 정한다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# namespace='CELERY'는 모든 셀러리 관련 구성 키를 의미한다. 반드시 CELERY라는 접두사로 시작해야 한다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 장고 app config에 등록된 모든 taks 모듈을 불러온다.
# app.autodiscover_tasks()
# from datetime import timedelta
#
# app.conf.beat_schedule={
#     'say_hello-every-seconds': {
#         'task': 'notice.tasks.say_hello',
#         'schedule': timedelta(seconds=1),
#         'args': ()
#     },
# }

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Asia/Seoul',
    CELERY_ENABLE_UTC=False,
    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler',
)

django.setup()

app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    app.start()