from django.contrib import admin

# Register your models here.
from stocks.models import IPO


@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ipo_id',
        "name",
        "schedule",
        "start_date",
        "end_date",
        "fixed_price",
        "hoped_price",
        "compete_rate",
        #"underwriter",
        "detail_link",
        'is_finished',
        'get_stocks',
    ]
    ordering = ['-end_date']
    def get_stocks(self,obj):
        return " \n".join([p.name for p in obj.stock_brokers.all()])

