from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','is_management')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional Info', {'fields': ( 'title', 'status', 'middle_name', 'job_title', 'department', 'office_location', 'room_number', 'plc_number', 'personal_number', 'staff_number')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'is_management', 'title', 'status', 'middle_name', 'job_title', 'department', 'office_location', 'room_number', 'plc_number', 'personal_number', 'staff_number'),
        }),
    )
    list_display = ( 'first_name', 'last_name', 'email','is_staff',  'is_active', 'is_management','is_superuser')  
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_management')
    search_fields = ( 'email', 'first_name', 'last_name')
    ordering = ('first_name',)

admin.site.register(User, CustomUserAdmin)
