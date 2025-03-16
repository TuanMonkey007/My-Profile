from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from hashids import Hashids

# Khởi tạo Hashids để tạo mã rút gọn
hashids_instance = Hashids(min_length=6, salt="your_secret_salt")

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"


@receiver(pre_save, sender=ShortURL)
def generate_short_code(sender, instance, **kwargs):
    if not instance.short_code:
        # Đảm bảo instance.id đã được gán
        if not instance.id:
            instance.id = ShortURL.objects.count() + 1
        
        while True:
            new_code = hashids_instance.encode(instance.id)
            if not ShortURL.objects.filter(short_code=new_code).exists():
                instance.short_code = new_code
                break
