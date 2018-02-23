from django.urls import path
from django.conf.urls import url
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #path('index', views.index, name='index'),
    #path('login', views.login, name='login')
    url(r'^login/', views.login, name='login')
]
