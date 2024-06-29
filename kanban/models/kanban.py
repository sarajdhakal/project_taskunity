from django.contrib.auth.models import User
from django.db import models

class Issue(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('new', 'New'),
        ('inprogress', 'In Progress'),
        ('review', 'Review'),
        ('done', 'Done'),
        ('unassigned', 'Unassigned'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unassigned')
    date_created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
