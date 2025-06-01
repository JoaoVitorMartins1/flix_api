from django.shortcuts import render
from rest_framework import generics
from .models import Actor
from .serializers import ActorsSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import ActorPermissionsClass

class ActorsCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,ActorPermissionsClass,)
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer


class ActorsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,ActorPermissionsClass,)
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer
