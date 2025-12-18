# listings/views.py

from django.views.generic import ListView, DetailView
from .models import Property

# 1. View for all properties (List View)
class PropertyListView(ListView):
    """
    Displays a list of all published properties, ordered by list_date.
    """
    model = Property
    template_name = 'listings/property_list.html' # Template will be created in the next step
    context_object_name = 'properties' # The name of the variable to use in the template
    paginate_by = 10 # Optional: Show 10 properties per page

    def get_queryset(self):
        # We can add filtering here later (e.g., filter by city, price, etc.)
        # For now, it simply orders by the latest listing date
        return Property.objects.all().order_by('-list_date')

# 2. View for a single property (Detail View)
class PropertyDetailView(DetailView):
    """
    Displays the details of a single property based on its primary key (pk).
    """
    model = Property
    template_name = 'listings/property_detail.html' # Template will be created in the next step
    context_object_name = 'property' # The name of the variable to use in the template