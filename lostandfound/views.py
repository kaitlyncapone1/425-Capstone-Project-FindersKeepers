from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render

def home(request):
    return render(request, 'lostandfound/home.html')

def about(request):
    return render(request, 'lostandfound/about.html')

def contact(request):
    return render(request, 'lostandfound/contact.html')
