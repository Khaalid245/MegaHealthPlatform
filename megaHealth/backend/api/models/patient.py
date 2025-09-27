from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    # Basic info
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)  # Male, Female, Other
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    blood_type = models.CharField(max_length=5, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    # Help Desk / system info
    patient_id = models.CharField(max_length=12, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    assigned_doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patients'
    )
    department = models.CharField(max_length=100, blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Auto-generate patient_id if not provided
        if not self.patient_id:
            self.patient_id = str(uuid.uuid4()).replace('-', '')[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_id})"
