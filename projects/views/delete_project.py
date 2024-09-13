from django.contrib import messages
from django.shortcuts import render,redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def delete_project(request, id):
    queryset = Project.objects.get(id = id)
    queryset.delete()
    messages.success(request, 'Project deleted successfully')
    return redirect('/project_list')

