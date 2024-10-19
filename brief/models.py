from django.db import models
from website.models import Domain

class List(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=2000)
    Photo = models.ImageField(upload_to='static/images/')

    def __str__(self) :
        return f'{self.Title}'


class Card(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=2000)
    Photo = models.ImageField(upload_to='static/images/')

    def __str__(self) :
        return f'{self.Title}'  


class Number(models.Model):
    Title = models.CharField(max_length=200)
    Number = models.IntegerField()
    Little = models.CharField(max_length=2000)

    def __str__(self) :
        return f'{self.Title}'  


class Brief(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=2000)
    Question = models.CharField(max_length=500)
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    List = models.ManyToManyField(
        List ,
        related_name='l_list',
        blank=True,
        help_text='Specific Title for list.',
        verbose_name='list')
    
    Card = models.ManyToManyField(
        Card ,
        related_name='c_card',
        blank=True,
        help_text='Specific Card for card.',
        verbose_name='card')
    
    Number = models.ManyToManyField(
        Number ,
        related_name='n_number',
        blank=True,
        help_text='Specific Title for number.',
        verbose_name='number')
    
    def __str__(self) :
        return f'{self.Title}'  


