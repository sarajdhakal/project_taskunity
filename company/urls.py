from django.urls import path
from company.views import company

urlpatterns = [
    path('company', company.company, name='company'),
]