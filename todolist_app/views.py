from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todolist(request):
    context = {
        'Welcome_text': 'welcome todo list page.'
    }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'Welcome_text': 'welcome contact page.'
    }
    return render(request, 'todolist.html', context)

def about(request):
    context = {
        'Welcome_text': 'welcome About page.'
    }
    return render(request, 'todolist.html', context)