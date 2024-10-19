from django.db import models
from website.models import Domain




# cards for about investment page
class Card (models.Model) :
    Card = models.CharField(max_length=200)


    def __str__(self):
        return self.Card

# all cards and title  for about investment page 
class Introcard (models.Model) :
    Title = models.CharField(max_length=1000)
    Card = models.ManyToManyField(
        Card ,
        related_name='Intro_card',
        blank=True,
        help_text='Specific Card for introcard.',
        verbose_name='introcard')
                                   
    Domain = models.ForeignKey(Domain ,to_field='domain' ,on_delete=models.CASCADE)
    def __str__(self):
        return self.Title
    

class IntroBanner(models.Model):
    Title = models.CharField(max_length=500)
    Discription = models.CharField(max_length=500)
    domain = models.ForeignKey(Domain ,to_field='domain' ,on_delete=models.CASCADE)
    Question = models.CharField(max_length=500)

    def __str__(self) :
        return f'{self.Title}'


class List(models.Model):
    List = models.CharField(max_length=5000)
    

    def __str__(self) :
        return f'{self.List}'
    
class IntroList(models.Model):
    Title = models.CharField(max_length=500)
    List = models.ManyToManyField(List, related_name= 'list_name', blank=True, help_text= 'help', verbose_name = 'introduction of list' )
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.Title}'
    







