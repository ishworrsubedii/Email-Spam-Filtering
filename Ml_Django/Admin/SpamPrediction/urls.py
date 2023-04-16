from . import views
from django.contrib import admin
from django.urls import path
from SpamPrediction import views


urlpatterns = [
    path('', views.modeleprediction, name='modelprediction'),
]
