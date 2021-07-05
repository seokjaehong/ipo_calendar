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
        "fixed_price",
        "hoped_price",
        "compete_rate",
        "underwriter",
        "detail_link",
        'is_finished',
    ]
    ordering = ['-ipo_id']
