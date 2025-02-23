from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from appWeb.profiles.models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ('avatar', 'bio', 'phone', 'social_links')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)