from rest_framework import serializers

from .models import*

#
class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = "__all__"
