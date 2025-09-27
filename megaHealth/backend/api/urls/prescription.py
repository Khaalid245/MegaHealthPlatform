from django.urls import path
from api.views.prescription import PrescriptionListView, PrescriptionDetailView

urlpatterns = [
    path('', PrescriptionListView.as_view(), name='prescription-list'),
    path('<int:pk>/', PrescriptionDetailView.as_view(), name='prescription-detail'),
]
