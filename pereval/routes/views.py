from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Routes
from .serializer import RoutesSerializer

class RoutesAPIView(APIView):
    def get(self,request):
        r = Routes.objects.all()
        return Response({'posts': RoutesSerializer(r, many=True).data})

    def post(self, request):
        serializer = RoutesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_routes = Routes.objects.create(
            titele=request.data['titele'],
            content=request.data['content'],
            )

        return Response({'post': model_to_dict(new_routes)})

#class RoutesAPIView(generics.ListAPIView):
#    queryset = Routes.objects.all()
#    serializer_class = RoutesSerializer