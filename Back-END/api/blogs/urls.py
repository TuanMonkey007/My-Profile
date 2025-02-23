from django.urls import path
from .views import BlogListCreateView, BlogDetailView

urlpatterns = [
    path('blog/', BlogListCreateView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view()),
]