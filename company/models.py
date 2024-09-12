from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
