from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ..forms import ProjectForm
from django.contrib.auth.decorators import login_required
from projects.models import Project
# @login_required(login_url='login')
def project_create(request):
    users = User.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        progress = request.POST.get('progress')
        price = request.POST.get('price')
        category = request.POST.get('category')
        team_member_ids = request.POST.getlist('team_member')

        project = Project.objects.create(
            name=name,
            description=description,
            image=image,
            status=status,
            due_date=due_date,
            progress=progress,
            price=price,
            category=category,
        )

        team_member = User.objects.filter(id__in=team_member_ids)
        project.team_member.set(team_member)  
        return redirect('/project_create')

    return render(request, 'project_create.html', {'users': users})
