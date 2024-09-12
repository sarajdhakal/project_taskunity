from django.urls import path
from .views import home, login, signup, forgot, coming_soon

urlpatterns = [
    path('', home.index, name='index'),
    path('login', login.user_login, name='login'),
    path('signup', signup.signup, name='signup'),
    path('logout', login.logoutUser, name='logout'),
    path('forgot', forgot.forgot, name='forgot'),
    path('coming_soon', coming_soon.coming_soon, name='coming_soon'),
]
