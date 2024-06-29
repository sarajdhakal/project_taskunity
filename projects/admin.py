from django.contrib import admin

# Register your models here.
from .models.projects import Project
from .models.employee import Employee

admin.site.register(Project)
admin.site.register(Employee)