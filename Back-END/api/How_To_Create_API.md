# Tóm gọn lại các bước để dùng Django REST framework (DRF):

1. Đăng ký Django REST framework

    - Thêm 'rest_framework' vào INSTALLED_APPS trong settings.py.
    - Đăng ký URLs API trong urls.py của appCore.

2. Tạo file serializers.py

   - Mục đích: Chuyển đổi dữ liệu giữa Django models ↔ JSON (API response/request).
   - Nó giống như forms.py nhưng dành cho API.
   - Dùng serializers.ModelSerializer để tránh phải viết - lại logic chuyển đổi dữ liệu.
3. Tạo file urls.py
    - Khai báo các đường dẫn API, thường dùng path() hoặc router của DRF.
4. Chỉnh file views.py

    - Mục đích: Định nghĩa API endpoint (cách xử lý request).
    - Dùng APIView, GenericAPIView, hoặc ViewSet.
    - Xử lý các phương thức HTTP: GET, POST, PUT, DELETE.
