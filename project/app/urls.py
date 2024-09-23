 
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
   path('index',views.index,name='index'),
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('register/',views.register, name='register'),
   path('login/',views.login, name='login'), 
   path('registerdata/',views.registerdata, name='registerdata'),
 ]
