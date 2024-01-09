from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateTodo
from .models import Todo


# Add Todo
def todos(request):
    if request.method == 'POST':
        form = CreateTodo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    context = {
        'form':CreateTodo(),
        'todos':Todo.objects.all()
    }
    return render(request, 'todos.html', context)

# Update Todo
def update_todo(request, id):
    try:
        task = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return redirect('todos')

    if request.method == 'POST':
        form = CreateTodo(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todos')
    print("ID:", id)
    print("Form Data:", request.POST)
    print("Todo Instance:", task)
    form = CreateTodo(instance=task)
    context = {
        'form': form,
        'todos': Todo.objects.all()
    }
    return render(request, 'todos.html', context)

    

# Delete Todo
def delete_todo(request, id):
    try:
        task = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return redirect ('todos')
    
    if request.method == "POST":
        task.delete()
        return redirect('todos')
    else:
        form = CreateTodo()
        context = {
                'form': form,
                'todos': Todo.objects.all()
            }
        return render(request, 'todos.html', context)
    
# Is Completed
def is_completed(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.isCompleted = True
        todo.save()
        return redirect('todos')
    todos = Todo.objects.all()
    return render(request, 'todos.html', {'todos': todos})


