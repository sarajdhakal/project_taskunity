from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project


# @login_required(login_url='login')
def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'index.html', context)
