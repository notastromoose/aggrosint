from django.urls import path
from django.http import HttpResponse

from .views import HomePageView, OperationsPageView, AnalystPageView, ReportPageView

urlpatterns = [
    path('dashboard/', AnalystPageView, name='analyst'),
    path('operations/', OperationsPageView, name='operations'),
    path('home/', HomePageView, name='home'),
    path('report/', ReportPageView, name='report'),
    path('', HomePageView, name='home')
    
]
