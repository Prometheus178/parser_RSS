from django.urls import path, include
from Parser import views

urlpatterns = [
    path('', views.parseRSS, name='parseRSS'),
]
