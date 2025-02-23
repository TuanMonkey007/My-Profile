from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from appCore.helpers import get_file_path


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)  # Mã hóa mật khẩu trước khi lưu
        else:
            raise ValueError("Password must be set")
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True or extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_staff=True and is_superuser=True")

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=get_file_path, blank=True)  # Ảnh đại diện
    bio = models.TextField(blank=True, null=True)  # Giới thiệu ngắn
    phone = models.CharField(max_length=20, blank=True, null=True)  # Số điện thoại
    social_links = models.JSONField(default=dict, blank=True)  # Mạng xã hội (Facebook, LinkedIn, GitHub,...)

    objects = CustomUserManager()
    
    # Mã hóa mật khẻu trước khi lưu => bat buoc phai co vi day la user custom
    def save(self, *args, **kwargs): 
        if self.pk and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)  # Đảm bảo mã hóa khi cập nhật
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username


