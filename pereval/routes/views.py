from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Routes
from .serializer import RoutesSerializer

class RoutesAPIList(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class RoutesAPIUpdate(generics.UpdateAPIView):
   queryset = Routes.objects.all()
   serializer_class = RoutesSerializer

class RoutesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Routes.objects.all()
   serializer_class = RoutesSerializer

# class RoutesAPIView(APIView):
#     def get(self,request):
#         r = Routes.objects.all()
#         return Response({'posts': RoutesSerializer(r, many=True).data})
#
#     def post(self, request):
#         serializer = RoutesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return  Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not id:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Routes.objects.get(id=id)
#         except:
#             return Response({"error": "Method PUT not allowed"})
#
#         serializer = RoutesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


#        new_routes = Routes.objects.create(
#           titele=request.data['titele'],
#            content=request.data['content'],
#            )
#
#        return Response({'post': model_to_dict(new_routes)})

