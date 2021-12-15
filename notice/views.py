# model를 import
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework.views import APIView


def start_task(request):
    schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS, )
    if PeriodicTask.objects.filter(name='daily_notice').exists():  # 'test_task'가 등록되어 있으면,
        p_test = PeriodicTask.objects.get(name='daily_notice')
        p_test.enabled = True  # 실행시킨다.
        p_test.interval = schedule
        p_test.save()
    else:  # 'test_task'가 등록되어 있지 않으면, 새로 생성한다
        PeriodicTask.objects.create(
            interval=schedule,  # 앞서 정의한 schedule
            name='daily_notice',
            task='notice.tasks.say_hello',
        )

