from django.db import models
from website.models import Domain

class Pop_Up(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/')
    exp_date = models.DateTimeField()
    description = models.CharField(max_length=300)
    Domain =  models.ForeignKey(Domain, on_delete=models.CASCADE)


class TelegramBot(models.Model) :
    Ip = models.CharField(max_length=1000, null=True , blank=True)
    CHAT_ID1 = models.CharField(max_length=20 , null=True , blank=True)
    CHAT_ID2 = models.CharField(max_length=20, null=True , blank=True)
    CHAT_ID3 = models.CharField(max_length=20, null=True , blank=True)
    CHAT_ID4 = models.CharField(max_length=20, null=True , blank=True)

