from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class User(AbstractUser,PermissionsMixin):
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
    )

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    is_staff = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    plc_number = models.CharField(max_length=10)
    personal_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    staff_number = models.CharField(max_length=10, unique=True)
    username=None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
    
    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"
    
    
 
