from django.contrib import admin

# Register your models here.
from .models import ShortURL



class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'created_at', 'access_count') 
    search_fields = ('short_code', 'original_url')
    list_filter = ('created_at', 'access_count')

admin.site.register(ShortURL, ShortURLAdmin)

