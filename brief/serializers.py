from rest_framework import serializers
from .models import List, Card, Number, Brief


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields ='__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'

class BriefSerializer(serializers.ModelSerializer):
    List = ListSerializer(many = True)
    Card = CardSerializer(many = True)
    Number = NumberSerializer(many = True)

    class Meta:
        model = Brief
        fields = '__all__'


