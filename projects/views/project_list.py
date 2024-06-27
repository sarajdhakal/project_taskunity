from django.shortcuts import render
from ..models.projects import Project

def project_list(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'project-list.html', {'projects': projects})
