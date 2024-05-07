from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('view/<int:id>', views.contactview, name='view'),
    path('delete/<int:id>', views.contactdelete, name='delete'),
    path('edit/<int:id>', views.contactedit, name='edit'),
    path('create', views.contactcreate, name='create'),
]
