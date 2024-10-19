from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.urls import path, include
from website import views as viewsWbsite
from rest_framework import routers
from introduction.views import IntroBannerViewset , IntrocardViewSet , IntroListViewset 
from chart.views import  BarchartViewset
from menu.views import SuperMenuViewSet
from structure.views import Pop_UpViewset
from superproduct.views import SuperProductViewSet
from vision.views import TabvisionViewset
from vision.views import ConsulationViewset
from brief.views import BriefViewSet
from bourse.views import SectionViewSet
from supercart.views import SuperCartViewSet,RoadmapViewSet
from filebrowser.sites import site
from django.conf.urls.static import static
from django.conf import settings
from education.views import TrainingCourseViewSet




router = routers.DefaultRouter()
router.register(viewset=viewsWbsite.InformationViewSet, prefix='information', basename='information')
router.register(viewset=viewsWbsite.BranchViewSet ,prefix='branch',basename='branch')
router.register(viewset=viewsWbsite.BusinessPartnersViewSet ,prefix='businessPartners',basename='businessPartners')
router.register(viewset=viewsWbsite.ContactUsViewSet ,prefix='contactus',basename='contactus')
router.register(viewset=viewsWbsite.GroupingViewSet ,prefix='grouping',basename='grouping')
router.register(viewset=viewsWbsite.HistoryOfCompaniesViewSet ,prefix='historyofcompanies',basename='historyofcompanies')
router.register(viewset=viewsWbsite.ProjectProgressViewSet ,prefix='ProjectProgress',basename='ProjectProgress')
router.register(viewset=viewsWbsite.IntroductionOfCompaniesViewSet ,prefix='introductionofcompanies',basename='introductionofcompanies')
router.register(viewset=viewsWbsite.NewsViewSet ,prefix='news',basename='news')
router.register(viewset=viewsWbsite.ProductsViewSet, prefix='products',basename='products')
router.register(viewset=viewsWbsite.SoloProductsViewSet, prefix='soloproducts', basename='solo_products')
router.register(viewset=viewsWbsite.QuestionsViewSet ,prefix='questions', basename='questions')
router.register(viewset=viewsWbsite.QuickAccessViewSet ,prefix='quickaccess',basename='quickaccess')
router.register(viewset=viewsWbsite.RelatedLinksViewSet ,prefix='relatedlinks',basename='relatedlinks')
router.register(viewset=viewsWbsite.SubscriptionViewSet ,prefix='Subscription',basename='Subscription')
router.register(viewset=viewsWbsite.SubjectSubscriptionViewSet ,prefix='SubjectSubscription',basename='SubjectSubscription')
router.register(viewset=viewsWbsite.SliderViewSet ,prefix='slider',basename='slider')
router.register(viewset=viewsWbsite.StatisticsViewSet ,prefix='statistics',basename='statistics')
router.register(viewset=viewsWbsite.GalleryPhotoViewSet ,prefix='galleryphoto',basename='galleryphoto')
router.register(viewset=viewsWbsite.GalleryVideoViewSet ,prefix='galleryvideo',basename='galleryvideo')
router.register(viewset=viewsWbsite.TypeOfContentViewSet ,prefix='typeofcontent',basename='typeofcontent')
router.register(viewset=viewsWbsite.EmailViewSet ,prefix='email',basename='email')
router.register(viewset=viewsWbsite.SendEmailViewSet ,prefix='sendemail',basename='sendemail')
router.register(viewset=viewsWbsite.ReceiveEmailViewSet ,prefix='receiveemail',basename='receiveemail')
router.register(viewset=viewsWbsite.NewsWithRoutViewSet ,prefix='newswithroute',basename='newswithroute')
router.register(viewset=viewsWbsite.NewsWithGroupingViewSet ,prefix='newswithgrouping',basename='newswithgrouping')
router.register(viewset=viewsWbsite.ChartViewSet ,prefix='chart',basename='chart')
router.register(viewset=viewsWbsite.MenuViewSet ,prefix='Menu',basename='Menu')
router.register(viewset=viewsWbsite.ContentTabsViewSet ,prefix='ContentTabs',basename='ContentTabs')
router.register(viewset=viewsWbsite.ContentComparisonViewSet ,prefix='ContentComparison',basename='ContentComparison')
router.register(viewset=viewsWbsite.ContentListViewSet ,prefix='ContentList',basename='ContentList')
router.register(viewset=viewsWbsite.LiveViewSet ,prefix='live',basename='live')
router.register(viewset=viewsWbsite.ProductNameViewSet ,prefix='productname',basename='productname')
router.register(viewset=viewsWbsite.SocialResponsibilityViewSet ,prefix='SocialResponsibility',basename='SocialResponsibility')
router.register(viewset=IntroBannerViewset ,prefix='introbanner',basename='introbanner')
router.register(viewset=IntrocardViewSet ,prefix='introcard',basename='introcard')
router.register(viewset=IntroListViewset,prefix='introlist',basename='introlist')
router.register(viewset=BarchartViewset,prefix='barchart',basename='barchart')
router.register(viewset=TabvisionViewset,prefix='tabvision',basename='tabvision') 
router.register(viewset=BriefViewSet,prefix='brief',basename='brief') 
router.register(viewset=SectionViewSet,prefix='bourse',basename='bourse') 
router.register(viewset=ConsulationViewset,prefix='consulation',basename='consulation')
router.register(viewset=SuperMenuViewSet ,prefix='supermenus',basename='supermenus')
router.register(viewset=Pop_UpViewset, prefix='Pop_Up', basename='Pop_Up')
router.register(viewset=SuperProductViewSet, prefix='superproduct', basename='superproduct')
router.register(viewset=RoadmapViewSet, prefix='roadmap', basename='roadmap')
router.register(viewset=SuperCartViewSet, prefix='supercart', basename='supercart')
router.register(viewset=TrainingCourseViewSet, prefix='training', basename='training')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('summernote/', include('django_summernote.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('tinymce/', include('tinymce.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
