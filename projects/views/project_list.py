from django.shortcuts import render
from ..models.projects import Project
from django.contrib import messages

def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    if request.GET.get('search'):
        # print(request.GET.get('search'))
        queryset =projects.filter(name__icontains = request.GET.get('search'))
        context = { 'projects': queryset}

        if not queryset.exists():
            messages.info(request, "No results found")

    return render(request, 'project-list.html', context)
