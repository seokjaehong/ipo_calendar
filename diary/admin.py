from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from diary.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        # 'user',
        'my_account_list',
        'schedule',
        'ipo',
        'is_possible',
        'is_finished',

    ]

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request).select_related('user', 'ipo')
        return qs.filter(user=request.user).order_by('-is_possible','ipo__is_finished','ipo__end_date')

    def my_account_list(self, request):
        return request.user.accounts_list

    def schedule(self, request):
        return request.ipo.schedule

    @admin.display(boolean=True)
    def is_finished(self, request):
        return request.ipo.is_finished
