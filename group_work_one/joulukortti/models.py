import os

from django.db import models
from django.contrib.auth.models import User

class XmasCard(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    drawing = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hex_value = models.CharField(max_length=7)  # To store values like '#ffffff'

    def __str__(self):
        return self.name
