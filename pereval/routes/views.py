from django.shortcuts import render
from rest_framework import generics

from .models import Routes
from .serializer import RoutesSerializer


# Create your views here.
class RoutesAPIView(generics.ListAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer