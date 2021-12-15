from django.db import models
from django.contrib.auth.models import AbstractUser

from config import settings

__all__ = (
    'StockBroker',
    'User',
)


class StockBroker(models.Model):
    """
    주간사
    """
    name = models.CharField(max_length=100)
    created = models.DateTimeField('생성시간', auto_now_add=True)
    updated = models.DateTimeField('수정시간', auto_now=True)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', max_length=255, blank=True)
    phone_number = models.CharField(
        verbose_name='Phone_number',
        max_length=100,
        blank=True,
        null=True,
    )
    is_get_email = models.BooleanField('메일수신 여부 체크', default=True)
    is_get_sms = models.BooleanField('sms수신 여부 체크', default=True)
    is_get_app_push = models.BooleanField('app push수신 여부 체크', default=True)
    is_usable = models.BooleanField('사용여부', default=True)

    created = models.DateTimeField('생성시간', auto_now_add=True)
    updated = models.DateTimeField('수정시간', auto_now=True)

    accounts = models.ManyToManyField(StockBroker)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

