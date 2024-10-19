from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from rest_framework.response import Response
from . import models
from . import serializer
import pandas as pd




class SuperCartViewSet(viewsets.ModelViewSet):
    queryset = models.SuperCart.objects.all()
    serializer_class = serializer.SuperCart
    def get(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
       

class RoadmapViewSet(viewsets.ModelViewSet):
    queryset = models.Roadmap.objects.all()
    serializer_class = serializer.Roadmap
    def get(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        df = pd.DataFrame(serializer.data)
        df = df.sort_values('Sort')
        df = df.to_dict()
        print(df)

        return response.Response(df)
    
       