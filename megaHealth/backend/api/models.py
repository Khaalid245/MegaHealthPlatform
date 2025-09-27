# from django.db import models
# from django.utils import timezone

# class Patient(models.Model):
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name  = models.CharField(max_length=120)
#     dob        = models.DateField(blank=True, null=True)
#     phone      = models.CharField(max_length=30, blank=True)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Doctor(models.Model):
#     name = models.CharField(max_length=150)
#     specialization = models.CharField(max_length=120, blank=True)
#     phone = models.CharField(max_length=30, blank=True)

#     def __str__(self):
#         return self.name

# class Appointment(models.Model):
#     patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='appointments')
#     doctor  = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, related_name='appointments')
#     scheduled_at = models.DateTimeField()
#     status = models.CharField(max_length=30, default='scheduled')
#     notes = models.TextField(blank=True, null=True)

#     class Meta:
#         ordering = ['-scheduled_at']

#     def __str__(self):
#         return f"{self.patient} - {self.scheduled_at}"

# class Consultation(models.Model):
#     patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='consultations')
#     doctor  = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
#     date = models.DateTimeField(default=timezone.now)
#     diagnosis = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)

# class Prescription(models.Model):
#     consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE, related_name='prescriptions')
#     medication = models.CharField(max_length=200)
#     dose = models.CharField(max_length=100, blank=True)
#     duration_days = models.IntegerField(null=True, blank=True)

# class LabResult(models.Model):
#     patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='labresults')
#     test_name = models.CharField(max_length=200)
#     result = models.JSONField(blank=True, null=True)
#     date = models.DateTimeField(default=timezone.now)
#     attachments = models.FileField(upload_to='lab_attachments/', blank=True, null=True)
