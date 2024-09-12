from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from projects.models import Project
from projects.models.employee import Employee
from ..models.kanban import Issue, Comment
from django.core.files.storage import default_storage
from django.contrib import messages

def kanban_issue(request, id):
    try:
        issue = get_object_or_404(Issue, id=id)
        projects = Project.objects.all()
        users = User.objects.all()
        employees = Employee.objects.all()
        comments = Comment.objects.filter(issue=issue)

        context = {
            'issue': issue,
            'projects': projects,
            'users': users,
            'employees': employees,
            'comments': comments,
        }

        if request.method == 'POST':
            if 'update_main_issue' in request.POST:
                title = request.POST.get('title')
                description = request.POST.get('description')
                status = request.POST.get('status')
                labels = request.POST.get('labels')
                project_name = request.POST.get('project').strip()
                desc = request.POST.get('issue_2description')
                attachments = request.FILES.getlist('attachment')
                due_date = request.POST.get('due_date')
                assigned_to_ids = request.POST.getlist('assigned_to')

                if not title:
                    messages.error(request, 'Title cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                if not project_name:
                    messages.error(request, 'Project name cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                project = Project.objects.filter(name__iexact=project_name).first()
                if not project:
                    messages.error(request, 'Please choose a valid project.')
                    return render(request, 'kanban_issue.html', context)

                if not description:
                    messages.error(request, 'Description cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                if not status:
                    messages.error(request, 'Status cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                if not desc:
                    messages.error(request, 'Issue description cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                if not labels:
                    messages.error(request, 'Labels cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                if not due_date:
                    messages.error(request, 'Due date cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                issue.title = title
                issue.description = description
                issue.status = status
                issue.labels = labels
                issue.project = project
                issue.issue_2description = desc
                issue.due_date = due_date

                for attachment in attachments:
                    file_path = default_storage.save(f'attachments/{attachment.name}', attachment)
                    issue.attachments.append(file_path)

                assigned_to = Employee.objects.filter(id__in=assigned_to_ids)
                issue.assigned_to.set(assigned_to)
                issue.save()
                messages.success(request, 'Issue updated successfully with attachments!')
                return redirect('kanban')

            elif 'create_child_issue' in request.POST:
                child_title = request.POST.get('title')
                child_description = request.POST.get('description')
                child_attachments = request.FILES.getlist('attachment')

                if not child_title:
                    messages.error(request, 'Child issue title cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                if not child_description:
                    messages.error(request, 'Child issue description cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                child_issue = Issue.objects.create(
                    title=child_title,
                    description=child_description,
                    status=issue.status,
                    labels=issue.labels,
                    project=issue.project,
                    due_date=issue.due_date,
                    user_id=request.user.id,
                )

                for attachment in child_attachments:
                    file_path = default_storage.save(f'attachments/{attachment.name}', attachment)
                    child_issue.attachments.append(file_path)

                child_issue.assigned_to.set(issue.assigned_to.all())
                child_issue.save()
                messages.success(request, 'Child issue created successfully!')
                return redirect('kanban')

            elif 'comment_form' in request.POST:
                user = request.user
                comment = request.POST.get('comment')
                issue = issue

                if not comment:
                    messages.error(request, 'Comment cannot be empty.')
                    return render(request, 'kanban_issue.html', context)

                comment = Comment.objects.create(
                    user=user,
                    issue=issue,
                    comment=comment
                )
                return render(request, 'kanban_issue.html', context)

        return render(request, 'kanban_issue.html', context)

    except Exception as e:
        print(f"Error: {e}")
        messages.error(request, f"An error occurred: {e}")
        return redirect('kanban')
