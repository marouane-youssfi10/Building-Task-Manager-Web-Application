from django.contrib import admin
from .models import Tasklist


class TaskListAdmin(admin.ModelAdmin):
    list_display = ('task', 'done', 'manage')

admin.site.register(Tasklist)

