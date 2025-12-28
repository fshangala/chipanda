# listings/views.py

from django.views.generic import ListView, DetailView
from .models import Property
from django.db.models import Q

class PropertyListView(ListView):
    model = Property
    template_name = 'listings/property_list.html'
    context_object_name = 'properties'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Capture GET parameters
        query = self.request.GET.get('q')
        province = self.request.GET.get('province')
        p_type = self.request.GET.get('type') # Rent or Sale

        # Text search (searches City, Area, and Province)
        if query:
            queryset = queryset.filter(
                Q(city__icontains=query) | 
                Q(area__icontains=query) | 
                Q(province__icontains=query)
            )

        # Province Filter
        if province:
            queryset = queryset.filter(province__iexact=province)

        # Property Type Filter (Matches 'RENT' or 'SALE')
        if p_type:
            queryset = queryset.filter(property_type__iexact=p_type)

        return queryset

# 2. View for a single property (Detail View)
class PropertyDetailView(DetailView):
    """
    Displays the details of a single property based on its primary key (pk).
    """
    model = Property
    template_name = 'listings/property_detail.html' # Template will be created in the next step
    context_object_name = 'property' # The name of the variable to use in the template