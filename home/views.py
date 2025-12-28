from django.views.generic import ListView
from listings.models import Property

class HomeView(ListView):
    model = Property
    template_name = 'home/index.html'
    context_object_name = 'featured_listings'
    paginate_by = 6

    def get_queryset(self):
        # Only show the 6 most recent published properties
        return Property.objects.all()