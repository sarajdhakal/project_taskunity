from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null = True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    salary = models.IntegerField()
    image = models.ImageField(upload_to = 'uploadedimages/users', default='1.png')
    def __str__(self):
        return self.name
