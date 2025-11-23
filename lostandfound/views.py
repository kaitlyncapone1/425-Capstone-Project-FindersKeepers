from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import FoundItem
from .forms import FoundItemForm
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactPostOwnerForm
from django.conf import settings
from django.contrib import messages
from .forms import EmailUserCreationForm

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
            found_item = form.save(commit=False) 
            found_item.user = request.user       
            found_item.save()   
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

#sends email: 
def contact_post_owner(request, post_id):
    post = get_object_or_404(FoundItem, id=post_id)
    owner_email = post.user.email  

    if request.method == "POST":
        form = ContactPostOwnerForm(request.POST)
        if form.is_valid():
            sender_email = form.cleaned_data['sender_email']
            message = form.cleaned_data['message']

            # send the email using Gmail setup
            try:
                send_mail(
                    subject=f"Inquiry about: {post.title}",
                    message=f"{message}\n\nReply to: {sender_email}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[owner_email],
                    fail_silently=False,
                )
                return redirect('contact_success')

            except Exception as e:
                # Show an error message on the same page
                messages.error(request, f"Error sending email: {e}")
    else:
        form = ContactPostOwnerForm()

    return render(request, 'lostandfound/contact_post_owner.html', {
        'form': form,
        'post': post
    })

def post_detail(request, post_id):
    post = get_object_or_404(FoundItem, id=post_id)
    return render(request, 'lostandfound/post_detail.html', {'post': post})

def contact_success(request):
    return render(request, 'lostandfound/contact_success.html')


def signup(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)  # or UserCreationForm
        try:
            if form.is_valid():
                form.save()
                return redirect("login")
        except Exception as e:
            # Catch any server-side exception (e.g., duplicate username)
            messages.error(request, f"Error creating account: {e}")
    else:
        form = EmailUserCreationForm()

    return render(request, "lostandfound/signup.html", {"form": form})
