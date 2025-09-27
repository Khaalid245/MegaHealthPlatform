from django.urls import path
from api.views.vitalsign import VitalSignListView, VitalSignDetailView

urlpatterns = [
    path('', VitalSignListView.as_view(), name='vitalsign-list'),
    path('<int:pk>/', VitalSignDetailView.as_view(), name='vitalsign-detail'),
]
