from django.contrib import admin
from .models import Patient, Doctor, Appointment, Consultation, Prescription, LabResult

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Consultation)
admin.site.register(Prescription)
admin.site.register(LabResult)
