from django.urls import path
from company.views import company

urlpatterns = [
    path('company', company.company, name='company'),
    path('all_events/', company.all_events, name='all_events'),
]