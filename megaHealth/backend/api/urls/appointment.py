from django.urls import path
from api.views.appointment import AppointmentListView, AppointmentDetailView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment-list'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]
