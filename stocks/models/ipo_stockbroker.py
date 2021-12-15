import json

from django.db import models

__all__ = (
    'IPOStockBroker',
)

from account.models import StockBroker
from stocks.models import IPO


class IPOStockBroker(models.Model):
    stock_broker = models.ForeignKey(StockBroker, on_delete=models.CASCADE, related_name='stock_broker_ipo_info_list')
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='ipo_stock_broker_info_list')

    def __str__(self):
        return f'주간사: {self.stock_broker}, IPO : {self.ipo}'
