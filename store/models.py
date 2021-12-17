from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField('태그명', max_length=10)
    created = models.DateTimeField('생성일', auto_now_add=True)
    updated = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    cat_choice = (
        ('한식', '한식'),
        ('중식', '중식'),
        ('양식', '양식'),
        ('일식', '일식'),
        ('기타', '기타'),
    )

    name = models.CharField('상호명', max_length=20)
    location = models.TextField('위치', blank=True, null=True)
    link = models.URLField('링크', blank=True, null=True)

    category = models.CharField(max_length=20, choices=cat_choice)
    menu = models.TextField('메뉴', blank=True, null=True)
    menu_img = models.ImageField('메뉴 이미지', blank=True, null=True)
    food_img = models.ImageField('음식 이미지', blank=True, null=True)

    tags = models.ManyToManyField(Tag)

    is_closed = models.BooleanField('폐점여부', default=False)
    description = models.TextField('기타', blank=True, null=True)

    created = models.DateTimeField('생성일', auto_now_add=True)
    updated = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def tag_list(self):
        return ", \n".join([p.name for p in self.tags.all()])
