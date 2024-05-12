from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    desciption = models.CharField(max_length=200, blank=False, null=False)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)
    
    def __str__(self):
        return self.title