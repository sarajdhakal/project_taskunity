from django.urls import path
from .views import home, login, signup, kanban, forgot


urlpatterns = [
    path('', home.index, name='index'),
    path('login', login.user_login, name='login'),
    path('signup', signup.signup, name='signup'),
    path('logout', login.logoutUser, name='logout'),
    path('kanban', kanban.kanban, name='kanban'),
    path('forgot', forgot.forgot, name='forgot'),
    # path('show', views.get_all_person)
]
