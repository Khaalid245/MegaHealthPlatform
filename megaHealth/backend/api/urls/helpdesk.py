# api/urls.py
from django.urls import path
from .views.helpdesk import HelpDeskView  # adjust path if your structure is different

urlpatterns = [
    # List all HelpDesk records or create a new record
    path('helpdesk/', HelpDeskView.as_view(), name='helpdesk-list'),

    # Retrieve, update, or delete a specific HelpDesk record by ID
    path('helpdesk/<int:pk>/', HelpDeskView.as_view(), name='helpdesk-detail'),
]
