from django.db import models

class FoundItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_found = models.DateField(auto_now_add=True)
    contact_info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    keywords = models.CharField(max_length=200, help_text="Comma-separated keywords for search")

    def __str__(self):
        return self.title