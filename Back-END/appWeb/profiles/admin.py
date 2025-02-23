from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from appWeb.profiles.models import CustomUser, Experience
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ('avatar', 'bio', 'phone', 'social_links')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('company_name', 'position')
    
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Experience, ExperienceAdmin)