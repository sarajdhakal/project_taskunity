from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from projects.models import Project
from projects.models.employee import Employee
from ..models.kanban import Issue
from django.core.files.storage import default_storage

def kanban_issue(request, id):
    try:
        issue = get_object_or_404(Issue, id=id)
        projects = Project.objects.all()
        users = User.objects.all()
        employees = Employee.objects.all()

        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            status = request.POST.get('status')
            labels = request.POST.get('labels')
            project_name = request.POST.get('project').strip()
            desc = request.POST.get('issue_2description')
            attachment = request.FILES.get('attachment', None)

            project = get_object_or_404(Project, name__iexact=project_name)

            issue.title = title
            issue.description = description
            issue.status = status
            issue.labels = labels
            issue.project = project
            issue.issue_2description = desc

            if attachment:

                if issue.attachment:
                    default_storage.delete(issue.attachment.path)
                issue.attachment = attachment
            issue.save()
            return redirect('kanban')

        context = {
            'issue': issue,
            'projects': projects,
            'users': users,
            'employees': employees
        }
        return render(request, 'kanban_issue.html', context)

    except Exception as e:
        print(f"Error: {e}")
        return redirect('kanban')
