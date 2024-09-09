from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from projects.models import Project
from ..models.kanban import Issue


# @login_required(login_url='login')
def kanban_issue(request, id):
    try:
        issue = Issue.objects.get(id=id)
        projects = Project.objects.all()
        users = User.objects.all()
        context = {
            'issue': issue,
            'projects': projects,
            'users': users,
        }
        return render(request, 'kanban_issue.html', context)
    except Exception as e:
        print(e)
