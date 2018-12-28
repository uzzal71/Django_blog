from django.shortcuts import render
from django.utils import timezone


posts = [
    {
        'author': 'Nasir Uddin',
        'title': 'Blog post one',
        'content': 'First blog post content',
        'date_posted': timezone.now()
    },
    {
        'author': 'Juwel Rana',
        'title': 'Blog post two',
        'content': 'Second blog post content',
        'date_posted': timezone.now()
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
