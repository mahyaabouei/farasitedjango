from rest_framework import serializers
from . import models
from persiantools.jdatetime import JalaliDate

class TrainingCourse (serializers.ModelSerializer) :
    Date = serializers.DateField(format='%Y-%m-%d')  
    jalali_date = serializers.SerializerMethodField()
    class Meta:
        model = models.TrainingCourse
        fields = ['Domain', 'Title', 'CreateAt', 'Date', 'Description', 'Duration', 'Teacher', 'Kind' , 'jalali_date']
       


    def get_jalali_date(self, obj):
        if obj.Date:  
            return JalaliDate.to_jalali(obj.Date).strftime('%Y/%m/%d')
        return None
