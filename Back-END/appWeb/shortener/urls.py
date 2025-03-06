from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShortURLViewSet, redirect_url, url_stats

router = DefaultRouter()
router.register(r'urls', ShortURLViewSet, basename='shorturl')

urlpatterns = [
    path('api/', include(router.urls)),  # API CRUD URLs
    path('<str:short_code>/', redirect_url, name='redirect'),  # Điều hướng URL
    path('<str:short_code>/stats/', url_stats, name='stats'),  # Thống kê lượt truy cập
]
