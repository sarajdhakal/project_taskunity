from django.shortcuts import render,redirect
from kanban.models import Issue
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def delete_kanban(request, id):
    queryset = Issue.objects.get(id = id)
    queryset.delete()
    messages.success(request,'Issue deleted successfully')
    return redirect('kanban')
