from .models import User, Article, Idea, Comment_Article, Comment_Idea
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'seniority', 'bio', 'title', 'status', 'public', 'password', 'pdp')

        widgets = {
            'title': forms.Select(attrs={'class': 'form-control',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de famille', 'id': 'last_name'}),
            'status': forms.Select(attrs={'class': 'position'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dis-en nous un peu plus sur toi!'}),
            'seniority': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Année d'entrée"}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'password': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Mot de passe", 'type': "password"}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =('title', 'description', 'URL_image', 'categories')
    
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
                'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
                'URL_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une image pour illustrer ton article"}),
                'categories': forms.Select(attrs={'class': 'form-control'}),
            }

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields =('title', 'description', 'URL_image', 'URL_video', 'categories')
    
    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'URL_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une image pour illustrer ton article"}),
            'URL_video': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "URL d'une vidéo pour illustrer ton article"}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
        }