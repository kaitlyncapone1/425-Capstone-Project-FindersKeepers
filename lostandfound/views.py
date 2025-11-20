from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FoundItem
from .forms import FoundItemForm

def landing(request):
    return render(request, 'lostandfound/landing.html')

def home(request):
    return render(request, 'lostandfound/home.html')

def about(request):
    return render(request, 'lostandfound/about.html')

def feed(request):
    return render(request, 'lostandfound/feed.html')

def main_feed(request):
    query = request.GET.get('q')
    if query:
        items = FoundItem.objects.filter(keywords__icontains=query)
    else:
        items = FoundItem.objects.all().order_by('-date_found')
    return render(request, 'lostandfound/main_feed.html', {'items': items})

@login_required
def upload_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_feed')
    else:
        form = FoundItemForm()
    return render(request, 'lostandfound/upload.html', {'form': form})