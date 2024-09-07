from django.urls import path
from analytics.views import analytics

urlpatterns = [
    path('analytics', analytics.analytics, name='analytics'),
]