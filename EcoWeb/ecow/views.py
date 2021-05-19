from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .forms import UserForm_one, UserForm_two, ArticleForm, IdeaForm, ProjectForm, Comment_IdeaForm, Comment_ArticleForm, Comment_ProjectForm, ImageForm
from .models import User, Article, Idea, Comment_Article, Comment_Idea, Project, Comment_Project, Image, Product
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Display
def index(request):
    # Send Email
    if request.method == 'POST':
        message = request.POST['message']
        subject = request.POST['subject']

        send_mail(subject, 
        message, 
        settings.EMAIL_HOST_USER, 
        ['eco.ambassadeurs.massignon@gmail.com'], 
        fail_silently = False)

    # Display users (team section)
    users = User.objects.all()[:4]
    return render(request, "ecow/index.html", {
        "users": users
    })

def command(request):
     # Send Email
    if request.method == 'POST':
        email = request.POST['email']
        option = request.POST['option']
        first_name = request.POST['first_name']
        last_name = request.POST ['last_name']

        subject = "COMMANDE ECO-BOUTIQUE"
        message = "Nouvelle commande de l'utilisateur. Nom: " + first_name + " - Prénom: " + last_name + " -  Article: " + option + ". Nous vous rapellons que les articles correspondants aux numéros ont été spécifiés aux Eco-ambassadeurs concernés."

        send_mail(subject, 
        message, 
        settings.EMAIL_HOST_USER, 
        ['eco.ambassadeurs.massignon@gmail.com'], 
        fail_silently = False)

        messages.success(request, 'Ta commande a bien été envoyée!')
        return HttpResponseRedirect(reverse("products"))

    # Display users (team section)
    users = User.objects.all()[:4]
    return render(request, "ecow/index.html", {
        "users": users
    })

def products(request):
    products = Product.objects.all
    return render(request, "ecow/products.html", {
        "products": products
    })


# Presentation display
def articles_display(request):
    # Display articles
    articles = Article.objects.all()
    return render(request, "ecow/presentation_layout.html", {
        "objects": articles,
        "type": "article"
    })

def articles_unique_display(request, key):
    try:
        articles = Article.objects.filter(categories=key)
    except Article.DoesNotExist:
        raise Http404("Article not found.")
    return render(request, "ecow/presentation_layout.html", {
        "objects": articles,
        "type": "article"
    })


def ideas_display(request):
    # Display projects)
    ideas = Idea.objects.all()
    return render(request, "ecow/presentation_layout.html", {
        "objects": ideas,
        "type": "idea"
    })

def projects_display(request):
    # Display projects
    projects = Project.objects.all()
    return render(request, "ecow/presentation_layout.html", {
        "objects": projects,
        "type": "project"
    })

def portfolio_display(request):
    articles_pics = Article.objects.all().values('URL_image')
    ideas_pics = Idea.objects.all().values('URL_image')
    projects_pics = Project.objects.all().values('URL_image', 'title')
    images_pics = Image.objects.all()
    length = len(images_pics)
    third = int(length/3)
    images_pics_one = Image.objects.all()[0:(third-1)].values('FIELD_image', 'title')
    images_pics_two = Image.objects.all()[third:(2*third-1)].values('FIELD_image', 'title')
    images_pics_three = Image.objects.all()[(2*third):(length-1)].values('FIELD_image', 'title')
    return render(request, "ecow/portfolio.html", {
        "articles_pics": articles_pics,
        "ideas_pics": ideas_pics,
        "projects_pics": projects_pics,
        "images_pics_one": images_pics_one,
        "images_pics_two": images_pics_two,
        "images_pics_three": images_pics_three,
    })


# Individual pages
def article(request, key):
    # If request method is Post => Save the comment 
    if request.method == "POST":
        form = Comment_ArticleForm(request.POST)
        if form.is_valid():
            # Add article id and user id and save
            comment = Comment_Article.objects.create(user=form.cleaned_data['user'], user_email=form.cleaned_data['user_email'], article=Article.objects.get(id=key), comment=form.cleaned_data['comment'])
            comment.save()
            # Return the page with the new comment and a success message
            messages.success(request, 'Ton commentaire a bien été créé!')
            return HttpResponseRedirect(reverse("article", kwargs={'key': key}))

        messages.warning(request, "Ton commentaire n'a pas été enregistré.")
        return HttpResponseRedirect(reverse("article", kwargs={'key': key}))

    # GET METHOD
    # Try to get the article info
    try:
        article = Article.objects.get(id=key)
    except Article.DoesNotExist:
        raise Http404("Article not found.")
    # Try to get the comments
    try:
        comments = Comment_Article.objects.filter(article_id=key)
    except Comment_Article.DoesNotExist:
        comments = False

    return render(request, "ecow/individual_layout.html", {
        "key": key,
        "object": article,
        "comments": comments,
        "type": "article",
        "form": Comment_ArticleForm(),
    })

def idea(request, key):
    if request.method == "POST":
        form = Comment_IdeaForm(request.POST)
        if form.is_valid():
            comment = Comment_Idea.objects.create(user=form.cleaned_data['user'], user_email=form.cleaned_data['user_email'], idea=Idea.objects.get(id=key), comment=form.cleaned_data['comment'])
            comment.save()
            messages.success(request, 'Ton commentaire a bien été créé!')
            return HttpResponseRedirect(reverse("idea", kwargs={'key': key}))

        messages.warning(request, "Ton commentaire n'a pas été enregistré.")
        return HttpResponseRedirect(reverse("idea", kwargs={'key': key}))

    try:
        idea = Idea.objects.get(id=key)
    except Idea.DoesNotExist:
        raise Http404("Listing not found.")
    try:
        comments = Comment_Idea.objects.filter(idea_id=key)
    except Comment_Idea.DoesNotExist:
        comments = False

    return render(request, "ecow/individual_layout.html", {
        "key": key,
        "object": idea,
        "comments": comments,
        "type": "idea",
        "form": Comment_IdeaForm(),
    })

def project(request, key):
    if request.method == "POST":
        form = Comment_ProjectForm(request.POST)
        if form.is_valid():
            comment = Comment_Project.objects.create(user=form.cleaned_data['user'], user_email=form.cleaned_data['user_email'], project=Project.objects.get(id=key), comment=form.cleaned_data['comment'])
            comment.save()
            messages.success(request, 'Ton commentaire a bien été créé!')
            return HttpResponseRedirect(reverse("project", kwargs={'key': key}))

        messages.warning(request, "Ton commentaire n'a pas été enregistré.")
        return HttpResponseRedirect(reverse("project", kwargs={'key': key}))

    try:
        project = Project.objects.get(id=key)
    except Project.DoesNotExist:
        raise Http404("Listing not found.")
    try:
        comments = Comment_Project.objects.filter(project_id=key)
    except Comment_Project.DoesNotExist:
        comments = False

    return render(request, "ecow/individual_layout.html", {
        "key": key,
        "object": project,
        "comments": comments,
        "type": "project",
        "form": Comment_ProjectForm(),
    })

def about_us(request):
    return render(request, "ecow/aboutus.html")

def credits(request):
    return render(request, "ecow/credits.html")


# CREATE
@login_required
def create(request):
    return render(request, "ecow/create.html")

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.create(user=User.objects.get(id=request.user.id), title=form.cleaned_data['title'], description=form.cleaned_data['description'], URL_image=form.cleaned_data['URL_image'], categories=form.cleaned_data['categories'])
            article.save()
            messages.success(request, 'Ton article a bien été créé!')
            return HttpResponseRedirect(reverse("articles"))

        return render(request, "ecow/new.html", {
        "form": ArticleForm(),
        "type": "Article",
        "URL": "create_article",
        "invalid": True
    })

    return render(request, "ecow/new.html", {
            'form': ArticleForm(),
            "type": "Article",
            "URL": "create_article"
    })

@login_required
def create_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = Idea.objects.create(user=User.objects.get(id=request.user.id), title=form.cleaned_data['title'], description=form.cleaned_data['description'], URL_image=form.cleaned_data['URL_image'], URL_video=form.cleaned_data['URL_video'], categories=form.cleaned_data['categories'])
            idea.save()
            messages.success(request, 'Ton tutoriel a bien été créé!')
            return HttpResponseRedirect(reverse("ideas"))

        return render(request, "ecow/new.html", {
        "form": IdeaForm(),
        "type": 'Tutoriel',
        "URL": "create_idea",
        "invalid": True
    })

    return render(request, "ecow/new.html", {
            'form': IdeaForm(),
            "type": 'Tutoriel',
            "URL": "create_idea"
    })

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.create(user=User.objects.get(id=request.user.id), title=form.cleaned_data['title'], description=form.cleaned_data['description'], URL_image=form.cleaned_data['URL_image'], URL_video=form.cleaned_data['URL_video'])
            project.save()
            messages.success(request, 'Ton projet a bien été créé!')
            return HttpResponseRedirect(reverse("projects"))

        return render(request, "ecow/new.html", {
        "form": ProjectForm(),
        "type": "Projet",
        "URL": "create_project",
        "invalid": True
    })

    return render(request, "ecow/new.html", {
            'form': ProjectForm(),
            "URL": "create_project",
            "type": "Projet"
    })

@login_required
def create_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.objects.create(user=User.objects.get(id=request.user.id), title=form.cleaned_data['title'], FIELD_image=form.cleaned_data['FIELD_image'])
            image.save()
            messages.success(request, 'Ton image a bien été ajoutée!')
            return HttpResponseRedirect(reverse("portfolio"))

        return render(request, "ecow/new.html", {
            "form": ImageForm(),
            "type": 'Image',
            "URL": "create_image",
            "invalid": True
    })

    return render(request, "ecow/new.html", {
            'form': ImageForm(),
            "type": 'Image',
            "URL": "create_image"
    })

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

@login_required
# Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register
def register(request):
    if request.method == "POST":
        form_one = UserForm_one(request.POST)
        form_two = UserForm_two(request.POST)
        if form_one.is_valid() and form_two.is_valid():
            username = form_one.cleaned_data['username']
            email = form_one.cleaned_data['email']
            first_name = form_one.cleaned_data['first_name']
            last_name = form_one.cleaned_data['last_name']
            seniority = form_one.cleaned_data['seniority']
            bio = form_one.cleaned_data['bio']
            status = form_two.cleaned_data['status']
            title = form_two.cleaned_data['title']
            public = form_two.cleaned_data['public']
            pdp = form_two.cleaned_data['pdp']

            code = request.POST["code"]

            if int(code) != 8985:
                return render(request, "ecow/register.html", {
                    "message": "Votre code d'accès est invalide. Veuillez nous contacter pour plus d'informations.",
                    "form": UserForm(),
                })

            # Ensure password matches confirmation
            password = form_two.cleaned_data['password']
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "ecow/register.html", {
                    "message": "Vos mots de passes sont différents.",
                    "form_one": UserForm_one(),
                    "form_two": UserForm_two,
                })

            # Attempt to create new user
            try:
                user = User.objects.create(username=username, email=email, password=password, first_name=first_name, last_name=last_name, seniority=seniority, bio=bio, status=status, title=title, pdp=pdp, public=public)
                user.save()
            except IntegrityError:
                return render(request, "ecow/register.html", {
                    "message": "Username déjà utilisé.",
                    "form_one": UserForm_one(),
                    "form_two": UserForm_two(),
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ecow/register.html", {
            "form_one": UserForm_one(),
            "form_two": UserForm_two,
        })