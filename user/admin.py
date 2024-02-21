from django.contrib import admin
from .models import User

@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('User Details', {
            'fields': ('email', 'username', 'first_name', 'last_name', 'created_at')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
    add_fieldsets = (
        ('User Details', {
            'fields': ('email', 'username', 'first_name', 'last_name', 'created_at')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )

    actions = ('activate_users', 'deactivate_users', 'make_staff',
               'make_superuser', 'remove_staff', 'remove_superuser')
