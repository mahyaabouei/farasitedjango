from rest_framework import serializers
from .models import ContentDrop , TabVision ,Consulation

class ContentDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDrop
        fields = ['Title' , 'Summer']


class TabvisionSerializer(serializers.ModelSerializer):
    Contentdrop = ContentDropSerializer(many = True)
    class Meta:
        model = TabVision
        fields = ['Title' , 'Summer' , 'Contentdrop' , 'Domain']


class ConsulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulation
        fields = '__all__'