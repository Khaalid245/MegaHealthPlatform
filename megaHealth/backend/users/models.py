from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('reception','Reception'),
        ('doctor','Doctor'),
        ('nurse','Nurse'),
        ('lab','LabTech'),
        ('patient','Patient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # admin approval
    must_change_password = models.BooleanField(default=False)  # optional

class StaffProfile(models.Model):
    STATUS = [('pending','Pending'), ('approved','Approved'), ('rejected','Rejected')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staffprofile')
    department = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_staff')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_staff')
    approved_at = models.DateTimeField(null=True, blank=True)

    def approve(self, admin_user):
        self.status = 'approved'
        self.user.is_active = True
        self.user.is_approved = True
        self.approved_by = admin_user
        self.approved_at = timezone.now()
        self.user.save()
        self.save()
    
    def reject(self, admin_user):
        self.status = 'rejected'
        self.approved_by = admin_user
        self.approved_at = timezone.now()
        self.user.is_active = False
        self.user.save()
        self.save()
