from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from projects.models import Project
from django.contrib import messages

# @login_required(login_url="/login/")
def update_project(request, id):
    try:
        project = Project.objects.get(id=id)
        team_member = project.team_member.all()
        users = User.objects.all()

        if request.method == "POST":
            name = request.POST.get('name')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            status = request.POST.get('status')
            extended_date = request.POST.get('extended_date')
            progress = request.POST.get('progress')
            price = request.POST.get('price')
            category = request.POST.get('category')
            team_member_ids = request.POST.getlist('team_member')

            
            if name=="":
                messages.error(request, 'Name cannot be empty.')
            elif description =="":
                messages.error(request, 'Description cannot be empty.')
            elif status == "":
                messages.error(request, 'Status cannot be empty.')
            elif progress =="":
                messages.error(request, 'Progress cannot be empty.')
            elif category =="":
                messages.error(request, 'Category cannot be empty.')
            elif price =="":
                messages.error(request, 'Price cannot be empty.')
            else:
                
                if extended_date:
                    project.extended_date = extended_date

                project.name = name
                project.description = description
                project.status = status
                project.progress = progress
                project.price = price
                project.category = category
                team_member = User.objects.filter(id__in=team_member_ids)
                project.team_member.set(team_member)

                if image:
                    project.image = image

                project.save()

                messages.success(request, 'Project updated successfully!')
                return redirect(f'/project_details/{project.id}/')

        context = {
            'project': project,
            'team_member': team_member,
            'users': users
        }

        return render(request, 'update_project.html', context)

    except Exception as e:
        print(e)
