from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('full_name', 'email', 'phone_number')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'phone_number', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'full_name', 'phone_number', 'is_staff')
    search_fields = ('username', 'email', 'full_name', 'phone_number')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)