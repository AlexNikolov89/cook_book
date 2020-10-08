from django.contrib.auth.models import User
from rest_framework import serializers

from cookbooks.models import Cookbook


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CookbookSerializer(serializers.ModelSerializer):
    #author = UserSerializer()

    class Meta:
        model = Cookbook
        fields = ('id', 'title', 'description', 'created', 'updated', 'author')