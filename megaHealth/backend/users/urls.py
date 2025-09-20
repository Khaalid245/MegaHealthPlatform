from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet, DoctorRegisterView, PatientList

# DRF router for staff management
router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')

urlpatterns = [
    path('', include(router.urls)),  # staff endpoints
    path('staff/register/', DoctorRegisterView.as_view(), name='doctor-register'),
    path('patients/', PatientList.as_view(), name='patients-list'),
]
