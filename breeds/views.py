# from django.shortcuts import render
from rest_framework import generics
from .serializer import BreedSerializer
from .models import Breeds
from breeds.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BreedList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticatedOrReadOnly,)
  queryset = Breeds.objects.all()
  serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Breeds.objects.all()
  serializer_class = BreedSerializer

