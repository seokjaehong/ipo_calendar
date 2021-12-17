# Create your models here.
from django.db import models

# Create your models here.
from account.models import User, StockBroker
from stocks.models import IPO


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE)

    comments = models.TextField('청약 추천내용', null=True, blank=True)
    is_possible = models.BooleanField('청약가능여부', default=False)

    order_cnt = models.IntegerField('청약신청수량', default=0)
    order_datetime = models.DateTimeField('청약신청 날짜', blank=True, null=True)
    order_stock_broker = models.ForeignKey(StockBroker, on_delete=models.CASCADE, blank=True, null=True)

    is_order = models.BooleanField('청약완료여부',default=False)
    description = models.TextField('비고', blank=True, null=True)

    created = models.DateTimeField('생성시간', auto_now_add=True)
    updated = models.DateTimeField('수정시간', auto_now=True)

    def __str__(self):
        return f'{self.user} + {self.ipo}'
