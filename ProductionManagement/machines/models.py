from django.db import models
from django.utils import timezone

class Machine(models.Model):
    name = models.CharField(max_length=100)
    pattern = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    info = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

