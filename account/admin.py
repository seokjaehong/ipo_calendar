from django.contrib import admin
from django.db import models
# Register your models here.

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.forms import CheckboxSelectMultiple

from .models import User, StockBroker


class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),

        (
            'Personal info',
            {'fields': (
                'first_name', 'last_name', 'phone_number', 'is_get_email', 'is_get_sms', 'is_get_app_push',
                'is_usable')}
        ),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Accounts', {'fields': ('accounts',)})
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'password1', 'password2'),
    #     }),
    # )
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'accounts_list',
    )
    search_fields = ('email', 'username',)
    ordering = ('email',)


    formfield_overrides = {
        models.ManyToManyField:{'widget':CheckboxSelectMultiple}
    }

admin.site.register(User, UserAdmin)
admin.site.register(StockBroker)