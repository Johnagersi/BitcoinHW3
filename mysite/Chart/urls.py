from django.conf.urls import url

from . import views
from django.views.generic import TemplateView



app_name = 'chart'
urlpatterns = [   
    url(r'^$', views.index, name='index'), 
]
