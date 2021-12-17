# Create your models here.
from django.db import models

# Create your models here.
from account.models import User
# from stocks.models import IPO
from store.models import Store


class Review(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    with_who = models.ManyToManyField(User)

    score = models.IntegerField('평점')
    description = models.TextField('비고', blank=True, null=True)

    created = models.DateTimeField('생성시간', auto_now_add=True)
    updated = models.DateTimeField('수정시간', auto_now=True)

    # @property
    # def get_with_who(self):
    #     return " \n".join([p.full_name for p in self.with_who.all()])

    def __str__(self):
        return f'{self.store}'
