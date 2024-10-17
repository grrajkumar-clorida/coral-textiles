from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Employees(AbstractUser):
    job_title = models.CharField(max_length=100)
    name = models.CharField(max_length=26)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    
    def __str__(self):
        return self.name
