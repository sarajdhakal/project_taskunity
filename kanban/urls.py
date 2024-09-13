from django.urls import path
from kanban.views import kanban, kanban_issue,delete_kanban, calendar

urlpatterns = [
    path('kanban', kanban.kanban, name='kanban'),
    path('kanban_issue/<id>/', kanban_issue.kanban_issue, name='kanban_issue'),
    path('calendar',calendar.calendar, name='calendar'),
    path('delete_kanban/<id>/', delete_kanban.delete_kanban, name='delete_kanban'),

]
