# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AgentCreationForm(UserCreationForm):
    """
    A custom form for creating new agent users.
    Inherits from UserCreationForm and adds email, first_name, and last_name fields.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email field required
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
