from django.db import models
from django.conf import settings
from django.utils import timezone

class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    specialization = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
