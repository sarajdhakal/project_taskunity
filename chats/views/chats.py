from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from chats.models import Room, Message, User


@login_required(login_url='login')
def rooms(request):
    rooms = Room.objects.all()
    users = User.objects.all()
    context = {'rooms': rooms, 'users': users}
    if request.method == "POST":
        name = request.POST.get('name')
        friends_ids = request.POST.getlist('friends')
        user1 = request.user

        if not name:
            messages.error(request, 'Chat Room name is required.')
            return render(request, 'chats.html', context)

        if not name:
            messages.error(request, 'Chat Room name is required.')
            return render(request, 'chats.html', context)

        if not friends_ids:
            messages.error(request, 'You must select at least one friend.')
            return render(request, 'chats.html', context)

        room = Room.objects.create(name=name, user1=user1)
        friends = User.objects.filter(id__in=friends_ids)
        room.friends.set(friends)
        messages.success(request, 'Successfully created room for chats.')
        return redirect('chats')

    return render(request, 'chats.html', context)


@login_required(login_url='login')
def room(request, slug):
    rooms = Room.objects.all()
    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))
    room_Desc = Room.objects.get(slug=slug)
    context = {'slug': slug,
               'rooms': rooms,
               'room_name': room_name,
               'messages': messages,
               'room_Desc': room_Desc
               }
    return render(request, "chat.html", context)
