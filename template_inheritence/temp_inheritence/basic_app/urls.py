from django.urls import path
from basic_app import views

# -*- coding: utf-8 -*-
urlpatterns = [
    path("relative/", views.relative, name= "relative"),  
    path("others/", views.others, name= "others"),
    path("base/", views.base, name= "base"),        
]