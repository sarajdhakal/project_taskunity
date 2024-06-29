from django.urls import path
from kanban.views import kanban

urlpatterns = [
    path('kanban', kanban.kanban, name='kanban'),
]