# accounts/views.py

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import AgentCreationForm

class RegisterView(FormView):
    """
    A view for new agents to register.
    On successful registration, the user is marked as staff and can log in to the admin.
    """
    template_name = 'accounts/register.html'
    form_class = AgentCreationForm
    success_url = reverse_lazy('admin:login') # Redirect to admin login page

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True # Mark the user as a staff member
        user.save()
        messages.success(self.request, "Agent account created successfully. You can now log in.")
        return super().form_valid(form)