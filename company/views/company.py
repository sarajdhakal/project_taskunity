from django.http import JsonResponse
from pyexpat.errors import messages
from django.contrib import messages
from company.models import Events
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def company(request):
    events = Events.objects.all()
    all_events = Events.objects.all()
    context = {'all_events': all_events}
    if request.method == 'POST':
        name = request.POST.get['name']
        location = request.POST.get['location']
        date = request.POST.get['date']
        start_time = request.POST.get['start_time']
        end_time = request.POST.get['end_time']
        description = request.POST.get['description']

        if not name:
            messages.error(request, 'Please enter Event name.')
            return render(request, 'company.html')
        if not location:
            messages.error(request, 'Please enter the location of the event.')
            return render(request, 'company.html')
        if not date:
            messages.error(request, 'Please enter the date of event .')
            return render(request, 'company.html')
        if not start_time:
            messages.error(request, 'Please enter company start time.')
            return render(request, 'company.html')
        if not end_time:
            messages.error(request, 'Please enter company end time.')
            return render(request, 'company.html')
        if not description:
            messages.error(request, 'Please enter company description.')
            return render(request, 'company.html')

        events.name = name
        events.location = location
        events.date = date
        events.description = description
        events.start_time = start_time
        events.end_time = end_time

        events.save()
        messages.success(request, 'Event successfully created.')
        return redirect('/calendar')
    return render(request, 'company.html', context)


@login_required(login_url='login')
def all_events(request):
    current_user = request.user
    all_events = Events.objects.all()
    filtered_events = []
    for event in all_events:
        if current_user.is_superuser or current_user in event.event_for.all() or not event.event_for.exists():
            filtered_events.append({
                'id': event.id,
                'name': event.name,
                'description': event.description,
                'location': event.location,
                'date': event.date.strftime('%Y-%m-%d'),
                'start_time': event.start_time.strftime('%H:%M:%S'),
                'end_time': event.end_time.strftime('%H:%M:%S'),
            })

    return JsonResponse(filtered_events, safe=False)


