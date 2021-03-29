from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasklist
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required # bach ta ila d5lti lpage todolist ou makntich loggin maraybrich id5lk
def todolist(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user # had ine bach t3rf user li zad task
            form.save()
        messages.success(request, 'New Task Added!')
        return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.filter(manage=request.user) # had line bach t5li l user ichof hi dakchi dyalo ou sf
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed.")
    return redirect('todolist')

@login_required
def edit_task(request, task_id):

    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, 'Task Edited!')
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)

        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def complate_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed.")
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

def index(request):
    context = {
        'index_text': 'welcome index page.'
    }
    return render(request, 'index.html', context)

@login_required
def contact(request):
    context = {
        'contact_text': 'welcome contact page.'
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': 'welcome About page.'
    }
    return render(request, 'about.html', context)