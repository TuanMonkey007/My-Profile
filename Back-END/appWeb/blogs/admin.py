from django.contrib import admin
from appCore.constants import APP_VALUE_ADMIN_MEDIA_JS
# Register your models here.

from .models import Blog, BlogPost

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ('title',)
    sortable_by = ('title',)
    class Media:
        js = APP_VALUE_ADMIN_MEDIA_JS

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'blog')
    search_fields = ('title',)
    sortable_by = ('title',)
    list_filter = ('status',)
    class Media:
        js = APP_VALUE_ADMIN_MEDIA_JS


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)