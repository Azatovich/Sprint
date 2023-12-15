from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
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

class RoutesAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2
class RoutesAPIList(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
class RoutesAPIUpdate(generics.RetrieveUpdateAPIView):
   queryset = Routes.objects.all()
   serializer_class = RoutesSerializer
   permission_classes = (IsAuthenticated, )

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

class UserAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = UserSerializer

class UserAPIUpdate(generics.UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = UserSerializer

class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = UserSerializer

class LevelAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = LevelSerializer

class LevelAPIUpdate(generics.UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = LevelSerializer

class LevelAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = LevelSerializer

class CoordsAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CoordsSerializer

class CoordsAPIUpdate(generics.UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = CoordsSerializer

class CoordsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CoordsSerializer