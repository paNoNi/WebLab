from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, DeleteView

from Auth.models import Profile
from sod.forms import TaskForm
from sod.models import UserTasks, Task

import datetime


def save_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
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
    else:
        form = TaskForm()
        context = {
            'form': form
        }

        return render(request, 'sod/addtask.html', context)


def get_usertask(request):
    pairs = UserTasks.objects.all()
    rem_date = dict()
    for pair in pairs:
        if pair.user_id == request.user.id:
            rem_date[pair.task.id] = (pair.task.date - datetime.date.today()).days
    return render(
        request,
        'sod/tasks.html',
        {'pairs_list': pairs,
         'rem_date': rem_date}
    )


class TaskDetailView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name_suffix = 'form'
    context_object_name = 'task'
    template_name = 'sod/UpdateTask.html'

    def get_success_url(self):
        return reverse('tasks')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'sod/DeleteTask.html'

    def get_success_url(self):
        return reverse('tasks')


class DescriptionDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'sod/description.html'
