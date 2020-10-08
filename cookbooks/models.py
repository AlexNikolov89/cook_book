from django.contrib.auth.models import User
from django.db import models


class Cookbook(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, related_name='cookbooks', on_delete=models.CASCADE, null=True)
    fans = models.ManyToManyField(to=User, related_name='c_favorite', blank=True)

    def __str__(self):
        return f'Cookbook {self.pk}: {self.title}'