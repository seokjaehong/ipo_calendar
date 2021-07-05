import time

import schedule
from rest_framework.views import APIView

from notice.telegram import job


class DoJob(APIView):
    def get(self, *args, **kwargs):
        schedule.every(5).seconds.do(job)
        print("start APP")

        while True:
            schedule.run_pending()
            time.sleep(1)

        return 0
