from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


handler404 = views.handler404

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('projects/', views.projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', views.projectDetail, name='projectDetail'),
    path('search/', views.search, name='search'),
]
