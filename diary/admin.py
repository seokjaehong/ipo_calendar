from django.db import models
# Register your models here.
from django.contrib import admin

# Register your models here.
from django.forms import CheckboxSelectMultiple

from diary.models import Order, Review


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = [
        'id',
        # 'user',
        'my_account_list',
        'schedule',
        'compete_rate',
        'ipo',
        'is_possible',
        'is_finished',
        'comments',
    ]

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request).select_related('user', 'ipo')
        return qs.filter(user=request.user).order_by('-is_possible', 'ipo__is_finished', 'ipo__end_date')

    def my_account_list(self, request):
        return request.user.accounts_list[:30] + "..."

    def schedule(self, request):
        return request.ipo.schedule

    def compete_rate(self, request):
        return request.ipo.compete_rate

    my_account_list.short_description = '나의 증권사 정보'

    compete_rate.short_description = '경쟁률'

    schedule.short_description = '청약 스케쥴'

    @admin.display(boolean=True)
    def is_finished(self, request):
        return request.ipo.is_finished

    is_finished.short_description = '청약 종료여부'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['store', 'get_persons', 'tags']
    list_per_page = 10
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }

    def get_persons(self, obj):

        return ", \n".join([p.full_name for p in obj.with_who.all()])

    def tags(self, obj):
        return obj.store.tag_list
