from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .models import FoundItem
from .forms import FoundItemForm

def landing(request):
    return render(request, 'lostandfound/landing.html')

def home(request):
    return render(request, 'lostandfound/home.html')

def about(request):
    return render(request, 'lostandfound/about.html')

def main_feed(request):
    query = request.GET.get('q')
    if query:
        items = FoundItem.objects.filter(keywords__icontains=query)
    else:
        items = FoundItem.objects.all().order_by('-date_found')
    return render(request, 'lostandfound/main_feed.html', {'items': items})

def upload_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_feed')
    else:
        form = FoundItemForm()
    return render(request, 'lostandfound/upload.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")   # or "main_feed" if you prefer
    else:
        form = AuthenticationForm()

    return render(request, "lostandfound/login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "lostandfound/signup.html", {"form": form})