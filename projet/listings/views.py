from django.shortcuts import render, redirect
from .models import Blog, Projet
from .forms import BlogForm, ProjetForm

# Create your views here.
def index(request):
    return render(request, 'listings/index.html')
def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog' : blog
    }
    return render(request, 'listings/blog.html', context)
def contact(request):
    return render(request, 'listings/contact.html')
def portfolio(request):
    projet = Projet.objects.all()
    context = {
        'projet' : projet
    }
    return render(request, 'listings/portfolio.html', context)
def forms(request):
    blogs = Blog.objects.all()
    projets = Projet.objects.all()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        projet_form = ProjetForm(request.POST)
        
        if blog_form.is_valid():
            blog = blog_form.save()
            return redirect('index')
        
        if projet_form.is_valid():
            projet = projet_form.save()
            return redirect('index')
    else:
        blog_form = BlogForm()
        projet_form = ProjetForm()
    return render(request, 'listings/forms.html', {'blog_form': blog_form, 'projet_form': projet_form,'blogs': blogs, 'projets': projets})