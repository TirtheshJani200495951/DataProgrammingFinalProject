from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book', views.book, name='book'),
    path('visuals', views.visualise, name='visualize'),
     path('v1', views.v1, name='vi'),
]