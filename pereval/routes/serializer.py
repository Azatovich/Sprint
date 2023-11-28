from rest_framework import serializers

from .models import*


class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = ('title', 'content', 'photo', 'time_create', 'time_update', 'is_published', 'cat')

