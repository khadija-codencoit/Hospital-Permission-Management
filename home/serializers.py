from rest_framework import serializers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLES_CHOICES)
    employee_id = serializers.CharField(max_length=100)
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=DoctorProfile.objects.all()
    )
    department = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):

        admin_code = validated_data.pop('admin_code', None)
        medical_history = validated_data.pop('medical_history', None)
        insurance_number = validated_data.pop('insurance_number', None)

        role = 'admin'

        user = User.objects.create_user(
            **validated_data,
            role=role
        )

        PatientProfile.objects.create(
            user=user,
            medical_history=medical_history,
            insurance_number=insurance_number
        )

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        feilds = ['id','username','email','role']

        def to_representation(self,instance):
            data = super().to_representation(instance)
            if instance.role == 'admin':
                data['profile'] = AdminProfile.objects.filter(user = instance).values().first()
            elif instance.role == 'patient':
                data['profile'] = DoctorProfile.objects.filter(user = instance).values().first()
            elif instance.role == 'staff':
                data['profile'] = PatientProfile.objects.filter(user = instance).values().first() 
 

            return super().to_representation(instance)
