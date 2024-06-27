from django.shortcuts import render


def forgot(request):
    return render(request, 'forgot.html')
