from django.urls import path
from user_list.views import user_list

urlpatterns = [
    path('user_list', user_list.user_list, name='user_list'),
]