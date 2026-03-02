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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_code = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username