from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone
from api.models import Patient, Appointment, Consultation, LabResult, VitalSign
from api.serializers import (
    PatientSerializer,
    AppointmentSerializer,
    ConsultationSerializer,
    LabResultSerializer,
    VitalSignSerializer
)

class PatientProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer

    def get_object(self):
        return self.request.user.patient_profile

class PatientAppointmentsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user.patient_profile).order_by('-scheduled_at')

    def perform_update(self, serializer):
        appointment = serializer.instance
        if appointment.scheduled_at <= timezone.now():
            raise PermissionDenied("Cannot update past appointments.")
        serializer.save()

class PatientConsultationsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        return Consultation.objects.filter(patient=self.request.user.patient_profile).order_by('-date')

class PatientLabResultsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LabResultSerializer

    def get_queryset(self):
        return LabResult.objects.filter(patient=self.request.user.patient_profile).order_by('-date')

class PatientVitalSignsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VitalSignSerializer

    def get_queryset(self):
        return VitalSign.objects.filter(patient=self.request.user.patient_profile).order_by('-date')
