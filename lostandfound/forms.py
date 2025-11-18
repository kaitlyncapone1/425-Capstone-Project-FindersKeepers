from django import forms
from .models import FoundItem

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['title', 'description', 'location', 'contact_info', 'keywords']