from django.shortcuts import render

def page_404(request):
    return render(request, 'pages_404.html')
