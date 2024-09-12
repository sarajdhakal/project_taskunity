from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user_list.html', context)

