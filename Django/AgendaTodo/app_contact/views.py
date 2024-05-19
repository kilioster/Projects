from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request, letter=None):
    if letter != None:
        contact = Contact.objects.filter(name__istartswith=letter) # filtro para buscar por letra
    else:
        contact = Contact.objects.filter(name__icontains=request.GET.get('search', '')) #filtro para buscar por texto
    
    context = {
        'contact': contact
    }
    return render(request, '../templates/app_contact/index.html', context)

def contactview(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, '../templates/app_contact/view.html', context)

def contactedit(request, id):
    contact = Contact.objects.get(id=id)
    
    if request.method == 'GET':
        form = ContactForm(instance = contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request, '../templates/app_contact/edit.html', context)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            return render(request, '../templates/app_contact/edit.html', {'form': form, 'id': id})

def contactdelete(request, id):
    contact = Contact.objects.get(id=id).delete()
    return redirect('contact')

def contactcreate(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, '../templates/app_contact/create.html', context)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            return render(request, '../templates/app_contact/create.html', {'form': form})