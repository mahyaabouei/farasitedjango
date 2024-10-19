from . import models
from rest_framework import serializers

class Pop_UpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pop_Up
        fields = '__all__'