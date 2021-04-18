from django.contrib import admin
from django.urls import path
from serveapp import views


urlpatterns = [
    path('', views.index),
    path('register/', views.registerPage),

]
