from django.contrib.auth.models import User
from company.models import Events
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url='login')
def calendar(request):
    today = timezone.now().date()
    print(today)
    all_events = Events.objects.all()
    today_events = Events.objects.filter(date=today)
    users = User.objects.all()
    context = {'all_events': all_events, 'users': users, 'today_events': today_events}

    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        description = request.POST.get('description')
        event_for_ids = request.POST.getlist('event_for')  # Get list of user IDs from form

        # Validation
        if not name:
            messages.error(request, 'Please enter Event name.')
            return render(request, 'calendar.html', context)
        if not location:
            messages.error(request, 'Please enter the location of the event.')
            return render(request, 'calendar.html', context)
        if not date:
            messages.error(request, 'Please enter the date of event.')
            return render(request, 'calendar.html', context)
        if not start_time:
            messages.error(request, 'Please enter event start time.')
            return render(request, 'calendar.html', context)
        if not end_time:
            messages.error(request, 'Please enter event end time.')
            return render(request, 'calendar.html', context)
        if not description:
            messages.error(request, 'Please enter event description.')
            return render(request, 'calendar.html', context)
        if not event_for_ids:
            messages.error(request, 'Select employees for this event.')
            return render(request, 'calendar.html', context)

        event = Events.objects.create(
            name=name,
            location=location,
            date=date,
            start_time=start_time,
            end_time=end_time,
            description=description
        )

        if 'all' in event_for_ids or not event_for_ids:
            event_for = User.objects.all()
        else:
            valid_event_for_ids = [id for id in event_for_ids if id.isdigit()]
            event_for = User.objects.filter(id__in=valid_event_for_ids)

        event.event_for.set(event_for)

        messages.success(request, 'Event successfully created.')
        return render(request, 'calendar.html', context)

    return render(request, 'calendar.html', context)
