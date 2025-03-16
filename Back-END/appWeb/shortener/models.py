import uuid
from django.db import models
from hashids import Hashids

hashids_instance = Hashids(min_length=6, salt="your_secret_salt")

class ShortURL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Nếu URL đã tồn tại => Lấy short_code cũ
        existing_record = ShortURL.objects.filter(original_url=self.original_url).first()
        if existing_record:
            self.short_code = existing_record.short_code
        else:
            # Nếu URL chưa có => Tạo short_code mới
            unique_id = str(uuid.uuid4())
            self.short_code = hashids_instance.encode(int(unique_id[:8], 16))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
