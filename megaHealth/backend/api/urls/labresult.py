from django.urls import path
from api.views.labresult import LabResultListView, LabResultDetailView

urlpatterns = [
    path('', LabResultListView.as_view(), name='labresult-list'),
    path('<int:pk>/', LabResultDetailView.as_view(), name='labresult-detail'),
]
