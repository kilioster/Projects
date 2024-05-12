from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.todoview, name='todo_view'),
    path('edit/<int:id>', views.todoedit, name='todo_edit'),
    path('delete/<int:id>', views.tododelete, name='todo_delete'),
    path('create', views.todocreate, name='todo_create'),
]
