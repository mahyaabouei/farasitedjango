from rest_framework import serializers
from .models import Content, Introduction, Card, Sections


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'



class ContentSerializer(serializers.ModelSerializer):
    Introduction = IntroductionSerializer (many = True)
    class Meta:
        model = Content
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class SectionsSerializer(serializers.ModelSerializer):
    Card = CardSerializer(many = True)
    Content = ContentSerializer(many = True)
    class Meta:
        model = Sections
        fields = '__all__'
        