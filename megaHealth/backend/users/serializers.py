from rest_framework import serializers
from .models import User, StaffProfile

class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = ['id','user','department','license_number','status','created_by','approved_by','approved_at']

class UserSerializer(serializers.ModelSerializer):
    staffprofile = StaffProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','role','phone','is_active','is_approved','staffprofile']

class StaffCreateSerializer(serializers.ModelSerializer):
    department = serializers.CharField(write_only=True, required=False)
    license_number = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username','email','password','role','phone','department','license_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        department = validated_data.pop('department', '')
        license_number = validated_data.pop('license_number', '')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False  # cannot login until approved
        user.is_approved = False
        user.save()
        StaffProfile.objects.create(user=user, department=department, license_number=license_number, created_by=self.context['admin_user'])
        return user
