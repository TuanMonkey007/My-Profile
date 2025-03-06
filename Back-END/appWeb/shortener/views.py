from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = "short_code"
    
    def create(self, request, *args, **kwargs):
        original_url = request.data.get("original_url")
        
        # Kiểm tra xem URL đã tồn tại chưa
        existing_url = ShortURL.objects.filter(original_url=original_url).first()
        if existing_url:
            return Response(
                {"message": "URL already shortened", "short_code": existing_url.short_code},
                status=status.HTTP_200_OK
            )
        
        # Nếu chưa tồn tại, tạo mới
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, short_code=None):
        url_instance = get_object_or_404(ShortURL, short_code=short_code)
        url_instance.access_count += 1
        url_instance.save()
        return Response({'original_url': url_instance.original_url})

    def update(self, request, short_code=None):
        url_instance = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(url_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, short_code=None):
        url_instance = get_object_or_404(ShortURL, short_code=short_code)
        url_instance.delete()
        return Response({'message': 'URL deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def redirect_url(request, short_code):
    url_instance = get_object_or_404(ShortURL, short_code=short_code)
    url_instance.access_count += 1
    url_instance.save()
    return HttpResponseRedirect(url_instance.original_url)

@api_view(['GET'])
def url_stats(request, short_code):
    url_instance = get_object_or_404(ShortURL, short_code=short_code)
    return Response({'short_code': short_code, 'access_count': url_instance.access_count})
