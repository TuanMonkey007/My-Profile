from django.db import models
from hashids import Hashids

# Khởi tạo Hashids để tạo mã rút gọn
hashids = Hashids(min_length=6, salt="your_secret_salt")

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = hashids.encode(len(ShortURL.objects.all()) + 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
