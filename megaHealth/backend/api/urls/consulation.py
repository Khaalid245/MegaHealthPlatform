from django.urls import path
from api.views.consultation import ConsultationListView, ConsultationDetailView

urlpatterns = [
    path('', ConsultationListView.as_view(), name='consultation-list'),
    path('<int:pk>/', ConsultationDetailView.as_view(), name='consultation-detail'),
]
