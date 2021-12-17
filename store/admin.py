from django.contrib import admin

# Register your models here.
from store.models import Store, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_per_page = 10
