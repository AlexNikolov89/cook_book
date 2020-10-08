from django.contrib.auth.models import User
from django.db import models

from cookbooks.models import Cookbook

choices = (('EASY', 'Easy'), ('INTERMEDIATE', 'Intermediate'), ('HARD', 'Hard'))

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    ingredients = models.TextField(blank=True)
    difficulty = models.CharField(max_length=20, choices=choices, default='Easy')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cookbook = models.ForeignKey(to=Cookbook, related_name='recipes', on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, related_name='recipes', on_delete=models.CASCADE, null=True)
    fans = models.ManyToManyField(to=User, related_name='r_favorite', blank=True)

    def __str__(self):
        return f'Recipe #{self.pk}: {self.title}'

