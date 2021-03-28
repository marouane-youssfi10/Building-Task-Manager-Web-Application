from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasklist

# Create your views here.

def todolist(request):

    all_tasks = Tasklist.objects.all

    return render(request, 'todolist.html', {'all_tasks': all_tasks})

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