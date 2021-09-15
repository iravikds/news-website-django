from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('api', views.news_list),
]
