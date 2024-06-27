from django.shortcuts import render
from projects.models import Project

def project_details(request, id):
    try:
        project = Project.objects.get(id=id)
        return render(request, 'project_details.html', {'project': project})
    except Exception as e:
       print(e)
