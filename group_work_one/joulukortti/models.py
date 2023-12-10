import os

from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    # Use os.path.basename to get only the filename
    filename = os.path.basename(filename)
    # Construct the upload path using only the filename
    return f'xmas_cards/{filename}'

class XmasCard(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    drawing = models.ImageField(upload_to=upload_to, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
