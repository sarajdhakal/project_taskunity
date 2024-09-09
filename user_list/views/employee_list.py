from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from projects.models.employee import Employee


# @login_required(login_url='login')
def employee_list(request):
    users = User.objects.all()
    employee = Employee.objects.all()
    context = {
        'users': users,
        'employee': employee
    }
    return render(request, 'employee_list.html', context)
