from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from ..forms import ProjectForm

def project_create(request):
    users = User.objects.all()
    # if request.method == 'POST':
    #     form = ProjectForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('project_list')
    # else:
    return render(request, 'project_create.html', {'user_list': users})
