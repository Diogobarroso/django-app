from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='index'),
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
]