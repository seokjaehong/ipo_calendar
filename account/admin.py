from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Member, MemberCompany


class MemberAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),

        (
            'Personal info',
            {'fields': (
                'first_name', 'last_name', 'phone_number', 'is_get_email', 'is_get_sms', 'is_get_app_push',
                'is_usable')}
        ),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'password1', 'password2'),
    #     }),
    # )
    list_display = ('username','first_name','last_name','email', 'is_staff', 'is_superuser',)
    search_fields = ('email', 'username',)
    ordering = ('email',)




admin.site.register(Member, MemberAdmin)
admin.site.register(MemberCompany)