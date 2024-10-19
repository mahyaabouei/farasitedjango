from rest_framework import viewsets
from .models import Brief
from .serializers import BriefSerializer
from rest_framework import serializers
from rest_framework import response

class BriefViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)