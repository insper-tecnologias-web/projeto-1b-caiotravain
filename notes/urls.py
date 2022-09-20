from turtle import update
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("delete",views.delete, name ="delete"),
    path("update", views.update, name="update"),
    path("atualiza", views.atualiza, name="atualiza"),
    path("tags", views.tags, name="tags"),
    path("unica",views.unica, name = 'unica')
]