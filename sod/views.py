from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
from sod.models import Task


class TaskView(View):

    def get(self, request):
        tasks = Task.objects.all()
        return render(
            request,
            'sod/tasks.html',
            {'task_list': tasks}
        )
