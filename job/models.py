from django.db import models
from .enum import TYPE_CHOICES, STATUS_CHOICES

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='full_time')
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='')
    date_applied = models.DateField(null=True, blank=True)
    date_updated = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company} ({self.status})"
    
