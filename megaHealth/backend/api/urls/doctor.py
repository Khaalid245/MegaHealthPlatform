from django.urls import path
from api.views.doctor import DoctorListView, DoctorDetailView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor-list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
]
