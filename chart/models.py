from django.db import models
from website.models import Domain


#  Funds for Barchart
class Fund (models.Model) :
    Title = models.CharField(max_length=500)
    Name = models.CharField(max_length=500)
    Efficiency = models.IntegerField()

    def __str__(self) :
        return f'{self.Title}'
    
#  Bar chart
class Barchart (models.Model) :
    Title = models.CharField(max_length=500)
    Description = models.CharField(max_length=2000)
    Fund = models.ManyToManyField (
    Fund,
    related_name= 'Fund_name', 
    blank=True, help_text= 'Specific Fund for Bar chart.', 
    verbose_name = 'introduction of Fund' )
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.Title}'