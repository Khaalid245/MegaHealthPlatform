from django.urls import path
from api.views.patient import (
    PatientProfileView,
    PatientAppointmentsView,
    PatientConsultationsView,
    PatientLabResultsView,
    PatientVitalSignsView
)

urlpatterns = [
    path('profile/', PatientProfileView.as_view(), name='patient-profile'),
    path('appointments/', PatientAppointmentsView.as_view(), name='patient-appointments'),
    path('consultations/', PatientConsultationsView.as_view(), name='patient-consultations'),
    path('labresults/', PatientLabResultsView.as_view(), name='patient-labresults'),
    path('vitalsigns/', PatientVitalSignsView.as_view(), name='patient-vitalsigns'),
]
