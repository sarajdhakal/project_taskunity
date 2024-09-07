from django.urls import path
from sales.views import sales

urlpatterns = [
    path('sales', sales.sales, name='sales'),
]