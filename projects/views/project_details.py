from django.shortcuts import render
from django.utils import timezone
from projects.models import Project
from kanban.models.kanban import Issue
from datetime import timedelta
from projects.models.employee import Employee
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def project_details(request, id):
    try:
        project = Project.objects.get(id=id)
        team_members = project.team_member.all()
        issues = Issue.objects.filter(project=project)
        labels = [issue.labels for issue in issues]
        total_tasks = issues.count()
        completed_tasks = issues.filter(status='done').count()
        total_hours_spent = timedelta()
        now = timezone.now()
        user_employee_images = {}
        for user in team_members:
            try:
                employee = user.employee
                user_employee_images[user] = employee.image.url
            except Employee.DoesNotExist:
                    user_employee_images[user] = None  

        for issue in issues:
            if issue.created_at.tzinfo is None:
                issue_created_at = timezone.make_aware(issue.created_at)
            else:
                issue_created_at = issue.created_at

            time_spent = now - issue_created_at
            total_hours_spent += time_spent

        total_hours_spent_in_hours = total_hours_spent.total_seconds() / 3600
        
        context = {
            'project': project,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'total_hours_spent': total_hours_spent_in_hours,
            'team_member': team_members,
            'user_employee_images': user_employee_images,
            'labels':labels
        }

        return render(request, 'project_details.html', context)
    except Exception as e:
        print(e)
