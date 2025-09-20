from .patient import PatientSerializer
from .nurse import NurseSerializer
from .doctor import DoctorSerializer
from .appointment import AppointmentSerializer
from .consultation import ConsultationSerializer
from .prescription import PrescriptionSerializer
from .labresult import LabResultSerializer
from .vitalsign import VitalSignSerializer

__all__ = [
    'PatientSerializer',
    'NurseSerializer',
    'DoctorSerializer',
    'AppointmentSerializer',
    'ConsultationSerializer',
    'PrescriptionSerializer',
    'LabResultSerializer',
    'VitalSignSerializer'
]
