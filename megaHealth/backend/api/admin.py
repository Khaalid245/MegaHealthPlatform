from django.contrib import admin
from .models.doctor import Doctor
from .models.nurse import Nurse
from .models.patient import Patient
from .models.appointment import Appointment
from .models.consultation import Consultation
from .models.labresult import LabResult
from .models.prescription import Prescription
from .models.vitalsign import VitalSign
from .models.helpdesk import HelpDesk  # corrected import

# Register models to admin site
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Consultation)
admin.site.register(LabResult)
admin.site.register(Prescription)
admin.site.register(VitalSign)
admin.site.register(HelpDesk)  # register HelpDesk
