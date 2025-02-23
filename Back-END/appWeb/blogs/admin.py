from django.contrib import admin
from appCore.constants import APP_VALUE_ADMIN_MEDIA_JS
# Register your models here.

from .models import Blog, BlogPost, BlogComment

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


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'user', 'comment', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    


    
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
