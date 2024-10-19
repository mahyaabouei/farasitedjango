from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializers





# Tab vision and summernote 
class TabvisionViewset(viewsets.ModelViewSet):
    queryset = models.TabVision.objects.all()
    serializer_class = serializers.TabvisionSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    

# Types of Consulation
class ConsulationViewset(viewsets.ModelViewSet):
    queryset = models.Consulation.objects.all()
    serializer_class = serializers.ConsulationSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    



