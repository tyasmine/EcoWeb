from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .forms import UserForm, ArticleForm, IdeaForm
from .models import User, Article, Idea, Comment_Article, Comment_Idea
from django.http import Http404

# Display
def index(request):
    users = User.objects.all()
    return render(request, "ecow/index.html", {
        "users": users,
    })

def articles_display(request):
    articles = Article.objects.all()
    return render(request, "ecow/articles.html", {
        "articles": articles,
    })

@login_required
def create(request):
    return render(request, "ecow/create.html")

@login_required
def create_object(request, key):
    if request.method == "POST":
        obj = request.POST['type']
        if obj == "article":
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = Article.objects.create(user=User.objects.get(id=request.user.id), title=form.cleaned_data['title'], description=form.cleaned_data['description'], URL_image=form.cleaned_data['URL_image'], categories=form.cleaned_data['categories'])
                article.save()
                return HttpResponseRedirect(reverse("index"))

            return render(request, "ecow/new.html", {
            "form": ArticleForm(),
            "invalid": True
        })
        else:
            form = IdeaForm(request.POST)
            if form.is_valid():
                idea = Idea.objects.create(user=User.objects.get(id=request.user.id), title=form.cleaned_data['title'], description=form.cleaned_data['description'], URL_image=form.cleaned_data['URL_image'], URL_video=form.cleaned_data['URL_video'], categories=form.cleaned_data['categories'])
                idea.save()
                return HttpResponseRedirect(reverse("index"))

            return render(request, "ecow/new.html", {
            "form": IdeaForm(),
            "invalid": True
        })

    if key == "article":
        return render(request, "ecow/new.html", {
            'form': ArticleForm(),
            'type': key,
        })
    elif key == "idea":
        return render(request, "ecow/new.html", {
            'form': IdeaForm(),
            'type': key,
        })
    else:
        raise Http404("Page not found.")

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
            public = form.cleaned_data['public']
            pdp = form.cleaned_data['pdp']

            code = request.POST["code"]

            if int(code) != 8985:
                return render(request, "ecow/register.html", {
                    "message": "Votre code d'accès est invalide. Veuillez nous contacter pour plus d'informations.",
                    "form": UserForm(),
                })

            # Ensure password matches confirmation
            password = form.cleaned_data['password']
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "ecow/register.html", {
                    "message": "Vos mots de passes sont différents.",
                    "form": UserForm(),
                })

            # Attempt to create new user
            try:
                user = User.objects.create(username=username, email=email, password=password, first_name=first_name, last_name=last_name, seniority=seniority, bio=bio, status=status, title=title, pdp=pdp, public=public)
                user.save()
            except IntegrityError:
                return render(request, "ecow/register.html", {
                    "message": "Username déjà utilisé.",
                    "form": UserForm(),
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ecow/register.html", {
            "form": UserForm(),
        })
