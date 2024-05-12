from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('<letter>/', views.contact, name='contact'),
    path('view/<int:id>', views.contactview, name='contact_view'),
    path('delete/<int:id>', views.contactdelete, name='contact_delete'),
    path('edit/<int:id>', views.contactedit, name='contact_edit'),
    path('create', views.contactcreate, name='contact_create'),
]
