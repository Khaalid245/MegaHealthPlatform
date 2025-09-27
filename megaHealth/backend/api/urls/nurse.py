from django.urls import path
from api.views.nurse import NurseListView, NurseDetailView

urlpatterns = [
    path('', NurseListView.as_view(), name='nurse-list'),
    path('<int:pk>/', NurseDetailView.as_view(), name='nurse-detail'),
]
