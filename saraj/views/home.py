import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.models.employee import Employee
from kanban.models.kanban import *


@login_required(login_url='login')
def index(request):
    logged_in_user = request.user
    try:
        employee = Employee.objects.get(user=logged_in_user)
        is_project_manager = employee.position == 'Project Manager'
    except Employee.DoesNotExist:
        is_project_manager = False

    projects = Project.objects.all()
    completed_count = Project.objects.filter(progress='Completed').count()
    pending_count = Project.objects.filter(progress__in=['Not started', 'In Progress']).count()
    web_development = Project.objects.filter(category='Web Development').count()
    android = Project.objects.filter(category='Android/IOS App').count()
    game = Project.objects.filter(category='Game Development').count()
    firewall = Project.objects.filter(category='Firewall').count()

    project_data = {
        'completed_count': completed_count,
        'pending_count': pending_count,
    }
    in_progress_count = Project.objects.filter(progress='In Progress')
    completed_count = Project.objects.filter(progress='Completed').count()
    delivered_count = Project.objects.filter(progress='Delivered').count()
    count = 0
    for project in projects:
        if project.extended_date == None:
            count = count + 1
    total = Project.objects.all().count()
    rate = count/total * 100
    completed_rate = int(rate)
    total_employees_count = Employee.objects.all().count()
    reviews_count = Issue.objects.filter(status="review").count()
    new_projects_count = Project.objects.filter(progress='Not started').count()
    done_count = completed_count + delivered_count
    context = {'projects': projects,
               'in_progress_count': in_progress_count,
               'completed_count': completed_count,
               'delivered_count': delivered_count,
               'completed_rate': completed_rate,
               'total_employees_count': total_employees_count,
               'reviews_count': reviews_count,
               'new_projects_count': new_projects_count,
               'project_data_json': json.dumps(project_data),
               'done_count': done_count,
               'is_project_manager': is_project_manager,
               'web_development': web_development,
               'android': android,
               'game': game,
               'firewall': firewall,
               }
    return render(request, 'index.html', context)
