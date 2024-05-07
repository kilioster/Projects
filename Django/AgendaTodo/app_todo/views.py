from django.shortcuts import render

# Create your views here.
def todo(request):
    return render(request, '../templates/app_todo/index.html', {})

def todoview(request):
    return render(request, '../templates/app_todo/view.html', {})

def todoedit(request):
    return render(request, '../templates/app_todo/edit.html', {})

def tododelete(request):
    return render(request, '../templates/app_todo/delete.html', {})

def todocreate(request):
    return render(request, '../templates/app_todo/create.html', {})