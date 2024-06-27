from django.shortcuts import render

def kanban(request):
    return render(request, 'kanban.html')
