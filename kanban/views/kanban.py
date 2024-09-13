from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from projects.models import Project
from ..forms import IssueForm, CommentForm
from ..models.kanban import Issue
from projects.models.employee import Employee


@login_required(login_url='login')
def kanban(request):
    logged_in_user = request.user
    try:
        employee = Employee.objects.get(user=logged_in_user)
        is_project_manager = employee.position == 'Project Manager'
    except Employee.DoesNotExist:
        is_project_manager = False
    if logged_in_user.is_superuser or is_project_manager:
        issues = Issue.objects.all()
    else:
        issues = Issue.objects.exclude(project__isnull=True)

    projects = Project.objects.all()
    users = User.objects.all()

    forms = {
        'todo': IssueForm(prefix='todo'),
        'new': IssueForm(prefix='new'),
        'inprogress': IssueForm(prefix='inprogress'),
        'unassigned': IssueForm(prefix='unassigned'),
        'review': IssueForm(prefix='review'),
        'done': IssueForm(prefix='done')
    }

    comment_form = CommentForm()
    form = IssueForm()

    if request.method == 'POST':
        for status in forms.keys():
            form = IssueForm(request.POST, prefix=status)
            if form.is_valid():
                issue = form.save(commit=False)
                issue.user = request.user
                issue.status = status
                issue.save()
                messages.success(request, 'Your issue has been created.')
                return redirect('kanban')

    context = {
        'forms': forms,
        'comment_form': comment_form,
        'form': form,
        'todo_issues': issues.filter(status='todo'),
        'new_issues': issues.filter(status='new'),
        'inprogress_issues': issues.filter(status='inprogress'),
        'unassigned_issues': issues.filter(status='unassigned'),
        'review_issues': issues.filter(status='review'),
        'done_issues': issues.filter(status='done'),
        'to_print': Issue.objects.all(),
        'projects': projects,
        'user_list': users,
        'is_project_manager': is_project_manager,
    }
    return render(request, 'kanban.html', context)
