from .models import User, Article, Idea, Comment_Article, Comment_Idea
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'seniority', 'bio', 'title', 'status', 'public', 'password', 'pdp')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de famille'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dis-en nous un peu plus sur toi!'}),
            'seniority': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Année d'entrée"}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'password': forms.TextInput(attrs={'class': "form-control", 'placeholder': "password"}),
        }