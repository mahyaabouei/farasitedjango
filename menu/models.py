from django.db import models
from website.models import Domain

# Create your models here.



class SubSuperMenu(models.Model):
    title = models.CharField(max_length=64)
    icon = models.ImageField (upload_to='static/images/')
    url = models.CharField(max_length=256)
    TYPE_CHOICES = (
        ('دکمه', 'Button'),
        ('لینک', 'link'),
    )
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    description = models.CharField(max_length=300,blank=True,null=True)
    Sort = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.title} {self.url}'

class SuperMenu(models.Model):
    domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    vector = models.ImageField (upload_to='static/images/', blank=True,null = True)
    sub = models.ManyToManyField(SubSuperMenu,blank=True)
    TYPE_CHOICES = (
        ('کشویی', 'dropdown'),
        ('لینک', 'link'),
    )
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    url = models.CharField(max_length=256,blank=True,null=True)
    
    

    