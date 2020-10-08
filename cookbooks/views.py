from django.db.migrations import serializer
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from cookbooks.models import Cookbook
from cookbooks.serializers import CookbookSerializer


class CookbookList(GenericAPIView):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data)

class ListUpdateDeleteCookbook(GenericAPIView):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    #lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.delete():
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
