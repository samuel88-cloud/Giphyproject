from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.quill,name='quill'),
    path('searchindex/',views.searchindex,name='searchindex'),
    path('search/',views.search,name='search'),
    path('next/',views.next,name='next'),
    path('search/addtoquill/<path:image>/',views.addtoquill,name='addtoquill'),
    path('next/addtoquill/<path:image>/',views.addtoquill),

]