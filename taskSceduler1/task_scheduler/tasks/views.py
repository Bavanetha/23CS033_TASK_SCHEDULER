# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm




def admin_task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/admin_task_list.html', {'tasks': tasks})

def delete_all_tasks(request):
    Task.objects.all().delete()
    return redirect('admin_task_list')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user_type = request.POST.get('user_type')
            task.created_by = request.user
            if user_type == 'worker':
                task.user_type = 'worker'
            elif user_type == 'tester':
                task.user_type = 'tester'
            task.save()
            
            return redirect('admin_task_list')  
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('admin_task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('admin_task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

def worker_task_list(request):
    worker_tasks = Task.objects.filter(user_type='worker')
    return render(request, 'tasks/worker_task_list.html', {'tasks': worker_tasks})

def tester_task_list(request):
    tester_tasks = Task.objects.filter(user_type='tester')
    return render(request, 'tasks/tester_task_list.html', {'tasks': tester_tasks})



# Create your views here.

def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()

    if task.user_type == 'worker' or task.user_type == 'Worker':
        return redirect('worker_task_list')
    elif task.user_type == 'tester' or task.user_type == 'Tester':
        return redirect('tester_task_list')


def admin_task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/admin_task_list.html', {'tasks': tasks})

def assign_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user_type = request.POST.get('user_type')
            task.assigned_to = user_type
            task.save()
            return redirect('admin_task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

