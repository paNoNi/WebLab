from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from Auth.models import Profile
from sod.forms import TaskForm
from sod.models import UserTasks


def get_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        user_id = request.user.id
        profile = Profile.objects.get(user_id=user_id)
        user_task = UserTasks()
        if form.is_valid():
            form.image = request.POST.get('image')
            form.save()
            user_task.user = profile
            user_task.task = form.instance
            user_task.save()
            return redirect(reverse('tasks'))

    form = TaskForm()
    context = {
        'form': form
    }

    return render(request, 'sod/addtask.html', context)


def get_usertask(request):
    pairs = UserTasks.objects.all()
    return render(
        request,
        'sod/tasks.html',
        {'pairs_list': pairs}
    )

