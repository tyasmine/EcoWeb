from .models import User, Article, Idea, Comment_Article, Comment_Idea, Project, Comment_Project, Image
from django.utils.translation import ugettext_lazy as _
from django import forms


class UserForm_one(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'seniority', 'bio')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de famille', 'id': 'last_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse Email'}),
            'seniority': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Année d'entrée"}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dis-en nous un peu plus sur toi!', 'rows': '5'}),
        }

        labels = {
            'first_name': _('Prénom'),
            'last_name': _('Nom de Famille'),
            'seniority': _("Année d'entrée"),
        }

class UserForm_two(forms.ModelForm):
    class Meta:
        model = User
        fields = ('title', 'status', 'public', 'pdp', 'password')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dis-en nous un peu plus sur toi!'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Mot de passe", 'type': "password"}),
        }

        labels = {
            'public': _("Publique"),
            'status': _("Statut"),
            'title': _("Titre"),
            'pdp': _("Photo de profil"),
            'password': _("Mot de passe"),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'URL_image', 'URL_video', 'categories',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'URL_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une image pour illustrer ton article"}),
            'URL_video': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une vidéo pour illustrer ton article"}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'title': _('Titre'),
            'categories': _('Catégorie'),
        }

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'description', 'URL_image', 'URL_video', 'categories',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'URL_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une image pour illustrer ton tutoriel"}),
            'URL_video': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une vidéo pour illustrer ton tutoriel"}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': _('Titre'),
            'categories': _('Catégorie'),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'URL_image', 'URL_video',)
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'URL_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une image pour illustrer ton projec"}),
            'URL_video': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une vidéo pour illustrer ton projet"}),
        }
            
        labels = {
            'title': _('Titre'),
        }

class Comment_ArticleForm(forms.ModelForm):
    class Meta:
        model = Comment_Article
        fields = ('user', 'user_email', 'comment',)
    
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ton nom'}),
            'user_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ton adresse-email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ton commentaire...'}),
        }

        labels = {
            'user': _("Nom d'utilisateur"),
            'user_email': _('Email'),
            'comment': _('Commentaire'),
        }

class Comment_IdeaForm(forms.ModelForm):
    class Meta:
        model = Comment_Idea
        fields = ('user', 'user_email', 'comment',)
    
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ton nom'}),
            'user_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ton adresse-email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ton commentaire...'}),
        }

        labels = {
            'user': _("Nom d'utilisateur"),
            'user_email': _('Email'),
            'comment': _('Commentaire'),
        }

class Comment_ProjectForm(forms.ModelForm):
    class Meta:
        model = Comment_Project
        fields = ('user', 'user_email', 'comment',)
    
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ton nom'}),
            'user_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ton adresse-email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ton commentaire...'}),
        }
        labels = {
            'user': _("Nom d'utilisateur"),
            'user_email': _('Email'),
            'comment': _('Commentaire'),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'FIELD_image')
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
        }

        labels = {
                'title': _("Titre"),
                'FIELD_image': _("Upload une image"),
        }