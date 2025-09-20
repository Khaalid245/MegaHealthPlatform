from rest_framework import generics, permissions
from api.models import Doctor
from api.serializers import DoctorSerializer

class DoctorListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.all()

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
