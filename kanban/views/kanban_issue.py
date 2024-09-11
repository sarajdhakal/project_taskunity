from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from projects.models import Project
from projects.models.employee import Employee
from ..models.kanban import Issue
from django.core.files.storage import default_storage
from django.contrib import messages

def kanban_issue(request, id):
    try:
        issue = get_object_or_404(Issue, id=id)
        projects = Project.objects.all()
        users = User.objects.all()
        employees = Employee.objects.all()
        context = {
            'issue': issue,
            'projects': projects,
            'users': users,
            'employees': employees
        }

        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            status = request.POST.get('status')
            labels = request.POST.get('labels')
            project_name = request.POST.get('project').strip()
            desc = request.POST.get('issue_2description')
            attachments = request.FILES.getlist('attachment')  # Get list of uploaded files
            due_date = request.POST.get('due_date')
            assigned_to_id = request.POST.get('assigned_to')

            if not title:
                messages.error(request, 'Title cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            if not project_name:
                messages.error(request, 'Project name cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            project_exists = Project.objects.filter(name__iexact=project_name).exists()

            if project_exists:
                project = Project.objects.get(name__iexact=project_name)
            else:
                messages.error(request, 'Please choose a valid project.')
                return render(request, 'kanban_issue.html', context)

            if not description:
                messages.error(request, 'Description cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            if not status:
                messages.error(request, 'Status cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            if not desc:
                messages.error(request, 'Description cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            if not labels:
                messages.error(request, 'Labels cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            if not due_date:
                messages.error(request, 'Date cannot be empty.')
                return render(request, 'kanban_issue.html', context)

            assigned_to = None
            if assigned_to_id:
                try:
                    assigned_to = Employee.objects.get(id=assigned_to_id)
                except Employee.DoesNotExist:
                    messages.error(request, 'Invalid employee selection.')
                    return render(request, 'kanban_issue.html', context)

            if status != 'unassigned' and issue.assigned_to is not None:
                messages.error(request, 'Assign people for the project.')
                return render(request, 'kanban_issue.html', context)

            issue.title = title
            issue.description = description
            issue.status = status
            issue.labels = labels
            issue.project = project
            issue.issue_2description = desc
            issue.due_date = due_date
            issue.assigned_to = assigned_to

            for attachment in attachments:
                file_path = default_storage.save(f'attachments/{attachment.name}', attachment)
                issue.attachments.append(file_path)  # Append each file path to the attachments list
            issue.save()

            messages.success(request, 'Issue updated successfully with attachments!')
            return redirect('kanban')

        return render(request, 'kanban_issue.html', context)

    except Exception as e:
        print(f"Error: {e}")
        return redirect('kanban')
