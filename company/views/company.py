from django.http import JsonResponse
from company.models import Events
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#@login_required(login_url='login')
def company(request):
    all_events = Events.objects.all()
    context = {'all_events': all_events}
    return render(request, 'company.html', context)

def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'location': event.location,
            'date': event.date.strftime('%Y-%m-%d'),
            'start_time': event.start_time.strftime('%H:%M:%S'),
            'end_time': event.end_time.strftime('%H:%M:%S'),
        })
        print(all_events)
    return JsonResponse(out, safe=False)

