from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    """Formulaire de création d'un compte avec un identifiant unique."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)
