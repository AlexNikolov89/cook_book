from django.contrib.auth.models import User
from rest_framework import serializers
from recipes.models import Recipe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RecipeSerializer(serializers.ModelSerializer):
   # author = UserSerializer(read_only=False)

    class Meta:
        model = Recipe
        fields = ('id', 'description', 'ingredients', 'difficulty', 'created', 'updated', 'cookbook', 'author')