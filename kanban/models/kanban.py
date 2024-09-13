from django.contrib.auth.models import User
from django.db import models
from projects.models import Project
from projects.models.employee import Employee
from ckeditor.fields import RichTextField


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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ManyToManyField(Employee, blank=True)
    attachments = models.JSONField(default=list, blank=True)
    labels = models.CharField(max_length=500, default='', blank=True)
    issue_2description = RichTextField(null=True, blank=True, default='')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
