from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complate/<task_id>', views.complate_task, name='complate_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),
]