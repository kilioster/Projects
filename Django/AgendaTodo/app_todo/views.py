from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo(request):
    todo = Todo.objects.filter(title__icontains=request.GET.get('search', ''))
    context = {
        'todo': todo
    }
    return render(request, '../templates/app_todo/index.html', context)

def todoview(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, '../templates/app_todo/view.html', context)

def todoedit(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == 'GET':
        form = TodoForm(instance = todo)
        context = {
            'form': form,
            'id': id
        }
        return render(request, '../templates/app_todo/edit.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            return redirect('todo')

def tododelete(request, id):
    todo = Todo.objects.get(id=id).delete()
    return redirect('todo')

def todocreate(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, '../templates/app_todo/create.html', context)
    
    if (request.method == 'POST'):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        