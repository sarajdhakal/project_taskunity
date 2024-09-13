from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ..forms import ProjectForm
from django.contrib.auth.decorators import login_required
from projects.models import Project
from django.contrib import messages


@login_required(login_url='login')
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

        if name =="":
            messages.error(request, 'Name cannot be empty.')
            
        elif description == "":
            messages.error(request, 'Description cannot be empty.')
        
        elif status =="":
            messages.error(request, 'Status cannot be empty.')

        elif due_date =="":
            messages.error(request, 'Due date cannot be empty.')

        elif progress =="":
            messages.error(request, 'Progress cannot be empty.')

        elif category =="":
            messages.error(request, 'Category cannot be empty.')

        
        elif price =="":
            messages.error(request, 'Budget cannot be empty.')

        else:
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
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')

    return render(request, 'project_create.html', {'users': users})
