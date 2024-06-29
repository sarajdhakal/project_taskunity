from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import IssueForm, CommentForm
from ..models.kanban import Issue


@login_required(login_url='login')
def kanban(request):
    issues = Issue.objects.all()
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
                messages.success(request, 'Your issue has been created as.')
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
    }
    return render(request, 'kanban.html', context)
