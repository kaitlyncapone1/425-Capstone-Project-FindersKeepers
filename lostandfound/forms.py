from django import forms
from .models import FoundItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['title', 'description', 'location', 'contact_info', 'keywords']
        exclude = ['user']

class ContactPostOwnerForm(forms.Form):
    sender_email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea)

class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]  # Make username the email
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user