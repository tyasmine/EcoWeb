from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .forms import UserForm
from .models import User, Article, Idea, Comment_Article, Comment_Idea


# Create your views here.
def index(request):
    return render(request, "ecow/index.html")

# Login
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ecow/login.html", {
                "message": "Votre username/mot de passe est invalide"
            })
    else:
        return render(request, "ecow/login.html")

# Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            seniority = form.cleaned_data['seniority']
            bio = form.cleaned_data['bio']
            status = form.cleaned_data['status']
            title = form.cleaned_data['title']

            code = request.POST["code"]

            if int(code) != 8985:
                return render(request, "ecow/register.html", {
                    "message": "Votre code d'accès est invalide. Veuillez vous refferez nous contacter pour plus d'informations."
                })

            # Ensure password matches confirmation
            password = form.cleaned_data['password']
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "ecow/register.html", {
                    "message": "Vos mots de passes sont différents."
                })

            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password, first_name, last_name, seniority, bio, status, title)
                user.save()
            except IntegrityError:
                return render(request, "ecow/register.html", {
                    "message": "Username déjà utilisé."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ecow/register.html", {
            "form": UserForm(),
        })

