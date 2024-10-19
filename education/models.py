from django.db import models
from website.models import Domain
from django.utils.timezone import now


class TrainingCourse (models.Model) :
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    Title = models.CharField(max_length=150)
    CreateAt = models.DateTimeField (default=now)
    Date  =models.DateField()
    Description  = models.CharField(max_length=5000 ,  null=True ,  blank=True)
    Duration = models.IntegerField()
    Teacher = models.CharField(max_length=150)
    Kind_Option = [
        ('online' , 'online'),
        ('in person' , 'in person'),
    ]
    Kind = models.CharField(max_length=10, choices=Kind_Option, default='in person')    
    def __str__(self):
        return str(self.Domain)+ '[' +self.Title+']'
    


