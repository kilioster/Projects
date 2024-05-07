from django.db import models
from datetime import date

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    mobile = models.CharField(max_length=13, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name