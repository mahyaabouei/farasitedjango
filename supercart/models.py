from django.db import models
from website.models import Domain
from colorfield.fields import ColorField


# super cart
class SuperCart(models.Model):
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Logo = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    Description = models.CharField(max_length=1500)
    Url1 = models.CharField(max_length=500, null=True, blank=True)
    Title_url1 = models.CharField(max_length=1500)
    Url2= models.CharField(max_length=500, null=True, blank=True)
    Title_url2 = models.CharField(max_length=1500)
    Url3= models.CharField(max_length=500, null=True, blank=True)
    Title_url3 = models.CharField(max_length=1500)
    Url4 = models.CharField(max_length=500, null=True, blank=True)
    Title_url4 = models.CharField(max_length=1500)
    Url5= models.CharField(max_length=500, null=True, blank=True)
    Title_url5 = models.CharField(max_length=1500)
    Url6= models.CharField(max_length=500, null=True, blank=True)
    Title_url6 = models.CharField(max_length=1500)
    Url7= models.CharField(max_length=500, null=True, blank=True)
    Title_url7 = models.CharField(max_length=1500)
    Url8= models.CharField(max_length=500, null=True, blank=True)
    Title_url8 = models.CharField(max_length=1500)
    Title_url9 = models.CharField(max_length=1500)
    Url9= models.CharField(max_length=500, null=True, blank=True)
    Url10= models.CharField(max_length=500, null=True, blank=True)
    Title_url10 = models.CharField(max_length=1500)
    Background_Color = ColorField (format="hexa" , default='#FFFFFF' , blank=True ,  null= True) 
    def __str__(self):
        return self.Title
    


# roadmap
class Roadmap(models.Model):
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    CartDescription = models.CharField(max_length=1500)
    Sort = models.IntegerField()
    Discription = models.CharField(max_length=1500)
    Color = ColorField (format="hexa" , default='#FFFFFF' , blank=True ,  null= True) 

    def __str__(self):
        return self.Title