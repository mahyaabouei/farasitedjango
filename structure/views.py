from django.shortcuts import render
from rest_framework import viewsets
from . import models
from rest_framework.response import Response
from rest_framework import status
from . import serializer
import datetime


class Pop_UpViewset(viewsets.ModelViewSet):
    queryset = models.Pop_Up.objects.all()
    serializer_class = serializer.Pop_UpSerializer
    def list(self,request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            return Response({'message':'Parameter "Domain" is required.'}, status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_queryset().first() 
        now = datetime.datetime.now().date() 
        if instance:
            serialized_data = self.get_serializer(instance).data
            exp_date_str = serialized_data.get('exp_date')
            exp_date = datetime.datetime.strptime(exp_date_str, "%Y-%m-%dT%H:%M:%SZ").date()
        if now > exp_date:
                return Response({'message': '[]'}, status=status.HTTP_200_OK)

        return Response(serialized_data, status=status.HTTP_200_OK)
    
        
        
        


            

    
