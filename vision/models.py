from django.db import models
from django_summernote.fields import SummernoteTextField
from website.models import Domain 
from tinymce.models import HTMLField


class ContentDrop(models.Model):
    Title = models.CharField(max_length=500)
    Summer = HTMLField()


    def __str__(self) :
        return self.Title
    

class TabVision (models.Model) :
    Title = models.CharField(max_length=200)
    Summer = HTMLField()
    Domain = models.ForeignKey (Domain , to_field='domain' , on_delete=models.CASCADE)
    Contentdrop = models.ManyToManyField (    
    ContentDrop,
    related_name= 'content_drop', 
    blank=True, help_text= 'Specific content for tab vision.', 
    verbose_name = 'summernot for content'  , 
    )

    def __str__(self):
        return self.Title
    

class Consulation(models.Model):
    Title = models.CharField(max_length=200)
    Discription = models.CharField(max_length=500)
    Photo = models.ImageField (upload_to='static/images/', blank=True, null=True)
    Domain = models.ForeignKey (Domain , to_field='domain' , on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
        


