from django.urls import path
from kanban.views import kanban, kanban_issue

urlpatterns = [
    path('kanban', kanban.kanban, name='kanban'),
    path('kanban_issue/<id>/', kanban_issue.kanban_issue, name='kanban_issue'),
]
