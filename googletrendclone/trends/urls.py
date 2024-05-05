from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
]
