from rest_framework import serializers
from .models import SuperProduct, SubSuperProduct

class SubSuperProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSuperProduct
        fields = '__all__'

class SuperProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuperProduct
        fields = '__all__'
