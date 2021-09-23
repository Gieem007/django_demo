from django.urls import path

from . import views

urlpatterns = [
    path('point', views.index, name='index'),
]