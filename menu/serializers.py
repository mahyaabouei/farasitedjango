from rest_framework import serializers
from .models import SubSuperMenu, SuperMenu


class SubSuperMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSuperMenu
        fields = '__all__'

class SuperMenuSerializer(serializers.ModelSerializer):
    sub = SubSuperMenuSerializer(many=True)

    class Meta:
        model = SuperMenu
        fields = '__all__'
