from django.urls import path
from .views import PatientDashboardView

urlpatterns = [
    path('patients/<int:pk>/dashboard/', PatientDashboardView.as_view(), name='patient-dashboard'),
]
