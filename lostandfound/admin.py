from django.contrib import admin
from .models import FoundItem

@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'location', 'date_found']
    list_filter = ['date_found']
    search_fields = ['title', 'description', 'keywords']