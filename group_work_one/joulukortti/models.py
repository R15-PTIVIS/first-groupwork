from django.db import models
from django.contrib.auth.models import User

class XmasCard(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    drawing_url = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
