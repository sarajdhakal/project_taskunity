from django.urls import path
from crm.views import crm

urlpatterns = [
    path('crm', crm.crm, name='crm'),
]