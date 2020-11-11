from django.contrib import admin
from .models import Task, UserTasks


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'object', 'date')
    list_filter = ('object', 'date')
    list_display_links = ('name', 'object')
    search_fields = ('name',)


@admin.register(UserTasks)
class UserTasksAdmin(admin.ModelAdmin):
    list_display = ('user', 'task')
    list_display_links = ('user', 'task')
