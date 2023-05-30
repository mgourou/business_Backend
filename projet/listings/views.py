from django.shortcuts import render
from .models import Blog, Projet

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