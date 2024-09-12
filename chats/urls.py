from django.urls import path
from chats.views import chats

urlpatterns = [
    path('chats', chats.rooms, name='chats'),
    path('<str:slug>/', chats.room, name='chats'),
]