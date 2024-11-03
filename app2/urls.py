from . import views
from django.urls import path

urlpatterns = [
    path('exit/', views.say_bye),
    path('exitfr/', views.say_buhbye),
    path('', views.home),
]