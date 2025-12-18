from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView

class RegisterView(FormView):
    form_class=UserCreationForm
    
    def form_valid(self, form):
        form.save()