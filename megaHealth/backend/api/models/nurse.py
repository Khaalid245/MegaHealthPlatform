from django.db import models
from django.conf import settings
from django.utils import timezone

class Nurse(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='nurse_profile'
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    sex = models.CharField(max_length=10, blank=True, null=True)  # Male, Female, Other
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # Can toggle access if needed
    department = models.CharField(max_length=120, blank=True, null=True)  # e.g., Triage, Ward

    def __str__(self):
        return f"Nurse {self.first_name} {self.last_name}"
