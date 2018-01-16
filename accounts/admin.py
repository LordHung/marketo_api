from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'password', 'full_name', 'is_active', 'staff', 'admin', )
    list_display = ('id', 'email', 'full_name', 'is_active', 'staff', 'admin', )
    list_display_links = ('id', 'email', 'full_name', )
    ordering = ('id', )
