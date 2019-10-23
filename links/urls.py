from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start_page, name="start_page"),
    path('<link>/', views.redirect_page, name="redirect_page"),
    path('<link>/stats', views.stats_page, name="stats_page"),
]
