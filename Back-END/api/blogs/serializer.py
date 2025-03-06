from rest_framework import serializers
from appWeb.blogs.models import Blog, BlogPost

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['id', 'title', 'slug', 'description', 'thumbnail', 'status']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'thumbnail', 'status']