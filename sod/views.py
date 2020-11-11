from django.shortcuts import render
from django.views.generic.base import View

from sod.models import UserTasks


class UserTasksView(View):

    def get(self, request):
        pairs = UserTasks.objects.all()
        return render(
            request,
            'sod/tasks.html',
            {'pairs_list': pairs}
        )

class AddTask(View):

    def get(self, request):
        return render(request, 'sod/addtask.html')