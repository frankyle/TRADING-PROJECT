from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # These are the fields that will be displayed in the admin list view
    list_display = ('email', 'first_name', 'second_name', 'phone_number', 'country', 'region', 'is_student', 'is_staff')
    
    # Fields that will be searchable in the admin search bar
    search_fields = ('email', 'first_name', 'second_name', 'phone_number')
    
    # Fields that will be available to filter the user list in the admin
    list_filter = ('country', 'region', 'is_student', 'is_staff')
    
    # These are the fields shown when editing/creating a user in the admin panel
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'second_name', 'phone_number', 'country', 'region', 'is_student')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to include when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'second_name', 'phone_number', 'country', 'region', 'is_student')}
        ),
    )

    ordering = ('email',)  # Orders users by their email in the admin panel

admin.site.register(User, CustomUserAdmin)
