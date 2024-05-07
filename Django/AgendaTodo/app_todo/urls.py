from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.todoview, name='view'),
    path('edit/<int:id>', views.todoedit, name='edit'),
    path('delete/<int:id>', views.tododelete, name='delete'),
    path('create', views.todocreate, name='create'),
]
