from django.contrib import admin
from . import models
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import News

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = News
        fields = '__all__'



# Register your models here.
admin.site.register(models.Information)
admin.site.register(models.BranchsOfCompany)
admin.site.register(models.BusinessPartners)
admin.site.register(models.ContactUs)
admin.site.register(models.Grouping)
admin.site.register(models.HistoryOfCompanies)
admin.site.register(models.ProjectProgress)
admin.site.register(models.IntroductionOfCompanies)
admin.site.register(models.News)
admin.site.register(models.Products)
admin.site.register(models.Questions)
admin.site.register(models.QuickAccess)
admin.site.register(models.RelatedLinks)
admin.site.register(models.SubjectSubscription)
admin.site.register(models.Subscription)
admin.site.register(models.Slider)
admin.site.register(models.Statistics)
admin.site.register(models.TypeOfContent)
admin.site.register(models.GalleryPhoto)
admin.site.register(models.GalleryVideo)
admin.site.register(models.Email)
admin.site.register(models.ReceiveEmail)
admin.site.register(models.SendEmail)
admin.site.register(models.Domain)
admin.site.register(models.positionofmanagers)
admin.site.register(models.ManagersPeople)
admin.site.register(models.Menu)
admin.site.register(models.ContentTabs)
admin.site.register(models.QaOfContentTabs)
admin.site.register(models.ContentComparison)
admin.site.register(models.ContentComparisonBtn)
admin.site.register(models.ContentList)
admin.site.register(models.ContentListChild)
admin.site.register(models.Live)
admin.site.register(models.GetFile)
admin.site.register(models.ProductName)
admin.site.register(models.SocialResponsibility)



