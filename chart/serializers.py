from rest_framework import serializers
from .models import Fund , Barchart



class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ['id', 'Title', 'Name', 'Efficiency']


class BarchartSerializer(serializers.ModelSerializer):
    Fund = FundSerializer(many=True)

    class Meta:
        model = Barchart
        fields = ['id', 'Title', 'Description', 'Fund', 'Domain']