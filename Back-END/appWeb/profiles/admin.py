from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from appWeb.profiles.models import *
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ('avatar', 'bio', 'phone', 'social_links')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('company_name', 'position')
    

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'major', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('school_name', 'degree', 'major')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('level',)
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    
    
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','date')
    list_filter = ('date',)
    search_fields = ('name', 'description')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'email', 'message')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Contact, ContactAdmin)