from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    """Crée un compte puis ouvre immédiatement sa session."""
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé.")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "authentication/signup.html", {"form": form})


@login_required
def home(request):
    """Affiche une page d'accueil pour l'utilisateur connecté."""
    return render(request, "authentication/home.html")
