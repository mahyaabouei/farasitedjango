from .models import SuperProduct , SubSuperProduct
from .serializer import SuperProductSerializer , SubSuperProductSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import serializers

class SuperProductViewSet(viewsets.ModelViewSet):
    queryset = SuperProduct.objects.all()
    serializer_class = SuperProductSerializer

    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_object = self.get_queryset().filter(Domain__domain=Domain)
        serialize = self.get_serializer(filtered_object, many=True)
        ser = serialize.data[0]
        for i in range (0,len(ser ['Super_Product']))  :
            sermodel = SubSuperProduct.objects.filter(id=ser ['Super_Product'][i]).first()
            print(sermodel)
            sermodel = SubSuperProductSerializer(sermodel).data
            print(sermodel)
            ser ['Super_Product'][i] = sermodel

        return Response(ser, status=status.HTTP_200_OK)




