from django.shortcuts import render
from appWeb.blogs.models import Blog, BlogPost
from rest_framework import generics
from .serializer import BlogSerializer

# Create your views here.

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer