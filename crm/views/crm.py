from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def crm(request):
    return render(request, 'crm.html')
