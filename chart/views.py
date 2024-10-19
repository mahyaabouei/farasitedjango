from rest_framework import viewsets
from .models import Barchart
from .serializers import  BarchartSerializer
from rest_framework import serializers
from rest_framework import response
import pandas as pd


def groupTitleBarChart (df):
    df = df[['Name','Efficiency']]
    df = df.to_dict('records')
    return df

class BarchartViewset (viewsets.ModelViewSet) :
    queryset = Barchart.objects.all()
    serializer_class = BarchartSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        serializer = serializer.data
        for i in serializer :
            df = pd.DataFrame(i['Fund'])

            df = df.groupby(by='Title').apply(groupTitleBarChart)
            df = df.reset_index()
            df = df.to_dict('records')
            i['Fund'] = df
        return response.Response(serializer)






