from website.models import Domain
from django.db import models

class Card(models.Model):
   Title = models.CharField(max_length=200)
   Description = models.CharField(max_length=2000) 
   photo  =models.ImageField(upload_to= 'static/images/', null=True , blank= True)

   def __str__(self) :
        return f'{self.Title}'

class Introduction(models.Model):
   Title = models.CharField(max_length=200)
   Description = models.CharField(max_length=2000) 
   Photo = models.ImageField(upload_to='static/images/' ,  null= True ,  blank= True)

   def __str__(self) :
        return f'{self.Title}'


class Content(models.Model):
   Name = models.CharField(max_length=200)
   Introduction = models.ManyToManyField(
        Introduction ,
        related_name='i_introduction',
        blank=True,
        help_text='Specific introduction for content.',
        verbose_name='introduction')
   
   def __str__(self) :
        return f'{self.Name}'

class Sections (models.Model):
   Title = models.CharField(max_length=200)
   Content = models.ManyToManyField(
        Content ,
        related_name='content',
        blank=True,
        help_text='Specific content for sections.',
        verbose_name='content')
   
   Card = models.ManyToManyField(
        Card ,
        related_name='cards',
        blank=True,
        help_text='Specific cards for sections.',
        verbose_name='card')
   
   Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)

   def __str__(self) :
        return f'{self.Title}'



