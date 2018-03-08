from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('list', views.list, name='list'),
    path('post_new', views.post_new, name='post_new'),
]