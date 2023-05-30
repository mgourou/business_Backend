from django import forms
from .models import Blog, Projet

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['nom', 'img', 'description']
        
class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'description']