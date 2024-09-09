from django.urls import path
from user_list.views import user_list, employee_list

urlpatterns = [
    path('user_list', user_list.user_list, name='user_list'),
    path('employee_list', employee_list.employee_list, name='employee_list'),
]