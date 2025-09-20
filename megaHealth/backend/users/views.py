from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import User, StaffProfile
from .serializers import UserSerializer, StaffCreateSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role__in=['doctor', 'nurse', 'lab', 'reception'])
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'create':
            return StaffCreateSerializer
        return UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['admin_user'] = self.request.user
        return context

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        staff_user = self.get_object()
        profile = staff_user.staffprofile
        profile.approve(request.user)
        return Response({'status': 'approved'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        staff_user = self.get_object()
        profile = staff_user.staffprofile
        profile.reject(request.user)
        return Response({'status': 'rejected'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        pending_staff = User.objects.filter(staffprofile__status='pending')
        serializer = UserSerializer(pending_staff, many=True)
        return Response(serializer.data)


class DoctorRegisterView(APIView):
    """
    Doctors can register themselves here.
    Their account will remain inactive until admin approves.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        data['role'] = 'doctor'
        serializer = StaffCreateSerializer(data=data, context={'admin_user': None})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'detail': 'Account created. Waiting admin approval.'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientList(ListAPIView):
    """
    Admin can view all patients.
    """
    queryset = User.objects.filter(role='patient')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
