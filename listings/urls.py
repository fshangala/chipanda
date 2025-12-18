# listings/urls.py

from django.urls import path
from .views import PropertyListView, PropertyDetailView

app_name = 'listings' # Namespace for reverse URL looking

urlpatterns = [
    # Path for the list of properties: e.g., /listings/
    path('', PropertyListView.as_view(), name='index'),
    
    # Path for an individual property: e.g., /listings/1/
    path('<int:pk>/', PropertyDetailView.as_view(), name='detail'),
]