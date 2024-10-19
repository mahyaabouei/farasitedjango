from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializer
import datetime
from website.models import Domain


class TrainingCourseViewSet(viewsets.ModelViewSet):
    queryset = models.TrainingCourse.objects.all()
    serializer_class = serializer.TrainingCourse
    def list(self, request):
        domain = request.query_params.get('Domain')
        if domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        domain_obj = Domain.objects.filter(domain =domain).first()
        filtered_objects = self.get_queryset().filter(Domain=domain_obj)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    





   