from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLES_CHOICES = [
        ('admin','admin'),
        ('doctor','doctor'),
        ('paitent','paitent'),
        ('staff','staff')
    ]
    role = models.CharField(max_length=20,choices=ROLES_CHOICES)

class AdminProfile(models.Model):
    user = models.OneToOneField(User,relatrd_name="admin_user", on_delete=models.CASCADE)
    admin_code = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class DoctorProfile(models.Model):
    user = models.OneToOneField(User,relatrd_name="doctor", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    licance_number = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)

class PaitentProfile(models.Model):
    user = models.OneToOneField(User,relatrd_name="doctor", on_delete=models.CASCADE)
    medical_history = models.TextField(null=True,Blank=True)
    insurance_number = models.CharField(max_length = 100)
