import json

from django.db import models

# Create your models here.


__all__ = (
    'IPO',
)

from account.models import StockBroker


class IPO(models.Model):
    name = models.CharField('종목명', max_length=20, default="")
    schedule = models.CharField('공모주일정', max_length=20, default="")
    fixed_price = models.IntegerField('확정공모가', default=0)
    hoped_price = models.CharField('희망공모가', max_length=30, default="")
    compete_rate = models.TextField('청약경쟁률', default="")
    underwriter = models.CharField('주간사리스트', max_length=100, default="")
    ipo_id = models.IntegerField("IPO ID", default=0)
    detail_link = models.URLField("IPO Detail링크", null=True, blank=True)
    start_date = models.DateField('시작일', blank=True, null=True)
    end_date = models.DateField('종료일', blank=True, null=True)

    is_finished = models.BooleanField('청약종료여부', default=False)

    created = models.DateTimeField('생성일', auto_now_add=True)
    updated = models.DateTimeField('수정일', auto_now=True)

    def set_underwriter(self, x):
        self.underwriter = json.dumps(x)

    def get_underwriter(self):
        return json.loads(self.underwriter)

    def save(self, *args, **kwargs):
        self.detail_link = "https://www.38.co.kr" + self.detail_link
        super(IPO, self).save()

    def __str__(self):
        return f'name: {self.name} ,일정: {self.schedule}, 확정가 : {self.fixed_price},희망가: {self.hoped_price},경쟁률 : {self.compete_rate}, 주간사: {self.underwriter} , 종료여부:{self.is_finished}, $시작일: {self.start_date}, $종료일: {self.end_date}'


