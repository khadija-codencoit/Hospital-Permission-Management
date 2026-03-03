from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class User(AbstractUser):
    ROLES_CHOICES = [
        ('admin','admin'),
        ('doctor','doctor'),
        ('paitent','paitent'),
        ('staff','staff')
    ]
    role = models.CharField(max_length=20,choices=ROLES_CHOICES)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, related_name="admin_user", on_delete=models.CASCADE)
    admin_code = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, related_name="doctor", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class PatientProfile(models.Model):
    user = models.OneToOneField(User, related_name="patient", on_delete=models.CASCADE)
    medical_history = models.TextField(null=True, blank=True)
    insurance_number = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
class StaffProfile(models.Model):
    user = models.OneToOneField(User, related_name="staff_profile", on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


def generate_number(*args, **kwargs):
    return str(uuid.uuid4()).split('-')[0].upper()

class Appointment(models.Model):
    appointment_number = models.CharField(
        max_length=100,
        unique=True,
        default=generate_number
    )
    scheduled = models.DateTimeField()
    remarks = models.CharField(max_length=255)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment_number