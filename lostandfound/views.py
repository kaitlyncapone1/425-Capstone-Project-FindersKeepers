from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    return render(request, 'lostandfound/landing.html')

def home(request):
    return render(request, 'lostandfound/home.html')

def about(request):
    return render(request, 'lostandfound/about.html')

@login_required
def feed(request):
    return render(request, 'lostandfound/feed.html')

