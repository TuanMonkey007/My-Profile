from django.db import models
from appCore.constants import *
from appCore.helpers import *
from tinymce.models import HTMLField
#how to install tinymce editor: pip install django-tinymce
from django.utils.text import slugify





# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='')
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to=get_file_path)
    status = models.CharField(max_length=200, choices=APP_VALUE_BLOG_STATUS, default=APP_VALUE_STATUS_DEFAULT)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
     

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='')
    content = HTMLField()
    thumbnail = models.ImageField(upload_to=get_file_path)
    status = models.CharField(max_length=200, choices=APP_VALUE_BLOG_STATUS, default=APP_VALUE_STATUS_DEFAULT)


    def save(self, *args, **kwargs):
        if not self.slug:  # Nếu slug chưa có, tự động tạo từ title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
      