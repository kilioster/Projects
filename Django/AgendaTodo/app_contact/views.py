from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    return render(request, '../templates/app_contact/index.html', {})

def contactview(request):
    return render(request, '../templates/app_contact/view.html', {})

def contactedit(request):
    return render(request, '../templates/app_contact/edit.html', {})

def contactdelete(request):
    return render(request, '../templates/app_contact/delete.html', {})

def contactcreate(request):
    return render(request, '../templates/app_contact/create.html', {})