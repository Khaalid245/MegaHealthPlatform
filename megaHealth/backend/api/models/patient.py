from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name  = models.CharField(max_length=120, null=True, blank=True)
    dob        = models.DateField(blank=True, null=True)
    sex        = models.CharField(max_length=10, blank=True, null=True)  # e.g., Male, Female, Other
    phone      = models.CharField(max_length=30, blank=True)
    address    = models.TextField(blank=True, null=True)
    email      = models.EmailField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    allergies  = models.TextField(blank=True, null=True)
    blood_type = models.CharField(max_length=5, blank=True, null=True)  # e.g., A+, O-
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
