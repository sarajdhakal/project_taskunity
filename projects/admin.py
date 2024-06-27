from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
# from projects.models import Project
from .models.projects import Project

admin.site.register(Project)