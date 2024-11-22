from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField( null=True)
    date_joined = models.DateField(null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_full_time = models.BooleanField(default=True, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    last_performance_review = models.DateTimeField(null=True, blank=True)
# Create your models here.

class ResetUuid(models.Model):
    UUID =models.UUIDField(unique=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    expiry = models.DateTimeField( null=True)