from django.shortcuts import render
from ..models.projects import Project
from kanban.models.kanban import Issue
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url='login')
def project_list(request):
    projects = Project.objects.all()

    if projects.exists():
        issues = Issue.objects.filter(project__in=projects)
        total_tasks = issues.count()
        completed_tasks = issues.filter(status='done').count()

        if total_tasks > 0:
            overall_percentage_completed = (completed_tasks / total_tasks) * 100
        else:
            overall_percentage_completed = 0

        project_percentage = {}

        # Loop through each project and calculate the percentage of completed tasks
        for project in projects:
            project_issues = issues.filter(project=project)
            total_project_tasks = project_issues.count()
            completed_project_tasks = project_issues.filter(status='done').count()

            # Calculate the percentage of completed tasks for the current project
            if total_project_tasks > 0:
                percentage_completed = (completed_project_tasks / total_project_tasks) * 100
            else:
                percentage_completed = 0

            # Store the percentage in the dictionary
            project_percentage[project.id] = int(percentage_completed)

        # Add the calculated percentages to the context
        context = {
            'projects': projects,
            'issues': issues,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'overall_percentage_completed': overall_percentage_completed,
            'project_percentage': project_percentage,
        }

        if request.GET.get('search'):
            queryset = projects.filter(name__icontains=request.GET.get('search'))
            context['projects'] = queryset

            if not queryset.exists():
                messages.info(request, "No results found")

    else:
        context = {
            'projects': projects,
            'issues': None,
            'total_tasks': 0,
            'completed_tasks': 0,
            'overall_percentage_completed': 0,
            'project_percentage': {},
        }

    return render(request, 'project-list.html', context)
