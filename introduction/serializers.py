from rest_framework import serializers
from .models import IntroBanner, IntroList, List ,Introcard 

class IntroBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroBanner
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['List']

class IntroListSerializer(serializers.ModelSerializer):
    List = serializers.SerializerMethodField()

    class Meta:
        model = IntroList
        fields = ['id', 'Title', 'Domain', 'List']

    def get_List(self, obj):
        return [list_item.List for list_item in obj.List.all()]


class IntrocardSerializer(serializers.ModelSerializer):
    Card = serializers.SerializerMethodField()

    class Meta:
        model = Introcard
        fields = ['id', 'Title', 'Domain', 'Card']
    def get_Card(self, obj):
        return [card.Card for card in obj.Card.all()]
    



