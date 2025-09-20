from django.db import models
from .patient import Patient
from django.utils import timezone

class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='labresults')
    test_name = models.CharField(max_length=200)
    result = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    attachments = models.FileField(upload_to='lab_attachments/', blank=True, null=True)
