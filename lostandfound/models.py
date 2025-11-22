from django.db import models
from django.contrib.auth.models import User

class FoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_found = models.DateField(auto_now_add=True)
    contact_info = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200, help_text="Comma-separated keywords for search")

    def __str__(self):
        return self.title