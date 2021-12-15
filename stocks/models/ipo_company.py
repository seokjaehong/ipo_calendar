import json

from django.db import models

__all__ = (
    'IPOCompany',
)

from account.models import Company
from stocks.models import IPO


class IPOCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_ipo_info_list')
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='ipo_company_info_list')

    def __str__(self):
        return f'주간사: {self.company}, IPO : {self.ipo}'
