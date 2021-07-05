import json

from django.db import models

# Create your models here.


__all__ = (
    'IPO',
)


class IPO(models.Model):
    name = models.CharField('종목명', max_length=20, default="")
    schedule = models.CharField('공모주일정', max_length=20, default="")
    fixed_price = models.IntegerField('확정공모가', default=0)
    hoped_price = models.CharField('희망공모가', max_length=30, default="")
    compete_rate = models.TextField('청약경쟁률', default="")
    underwriter = models.CharField('주간사리스트', max_length=100, default="")
    ipo_id = models.IntegerField("IPO ID", default=0)
    detail_link = models.URLField("IPO Detail링크", null=True, blank=True)

    is_finished = models.BooleanField('청약종료여부', default=False)

    created = models.DateTimeField('생성일', auto_now=True)
    updated = models.DateTimeField('생성일', auto_now_add=True)

    def set_underwriter(self, x):
        self.underwriter = json.dumps(x)

    def get_underwriter(self):
        return json.loads(self.underwriter)

    def save(self, *args, **kwargs):
        self.detail_link = "https://www.38.co.kr" + self.detail_link

        super(IPO, self).save()
