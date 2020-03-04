from django.shortcuts import render, get_object_or_404
from django.db import models
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models
from . import serializers      

class UserViewSet(viewsets.ViewSet):
    serializer_class = serializers.UserSerializer
    
    def list(self, request):
        queryset = models.CustomUser.objects.filter(id=request.user.pk)
        user = get_object_or_404(queryset)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

