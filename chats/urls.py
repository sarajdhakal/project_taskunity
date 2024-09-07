from django.urls import path
from chats.views import chats

urlpatterns = [
    path('chats', chats.chats, name='chats'),
]