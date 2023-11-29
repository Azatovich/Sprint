from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Routes, Category, User, Level, Coords
from .permission import IsAdminOrReadOnly, IsOnwerOrReadOnly
from .serializer import RoutesSerializer, CategorySerializer, UserSerializer, LevelSerializer, CoordsSerializer


# class RoutesViewSet(viewsets.ModelViewSet):
#     queryset = Routes.objects.all()
#     serializer_class = RoutesSerializer
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class LevelViewSet(viewsets.ModelViewSet):
#     queryset = Level.objects.all()
#     serializer_class = LevelSerializer
#
# class CoordsViewSet(viewsets.ModelViewSet):
#     queryset = Coords.objects.all()
#     serializer_class = CoordsSerializer


class RoutesAPIList(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
class RoutesAPIUpdate(generics.RetrieveUpdateAPIView):
   queryset = Routes.objects.all()
   serializer_class = RoutesSerializer
   permission_classes = (IsOnwerOrReadOnly, )

class RoutesAPIDestroy(generics.RetrieveDestroyAPIView):
   queryset = Routes.objects.all()
   serializer_class = RoutesSerializer
   permission_classes = (IsAdminOrReadOnly, )

class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryAPIUpdate(generics.UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class CategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer


