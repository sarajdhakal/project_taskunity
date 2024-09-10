from django.shortcuts import render,redirect
from projects.models import Project

def delete_project(request, id):
    queryset = Project.objects.get(id = id)
    queryset.delete()
    return redirect('/project_list')
