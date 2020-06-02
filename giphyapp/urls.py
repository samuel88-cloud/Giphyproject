from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.quill),
    path('index/',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('next/',views.next,name='next'),


]