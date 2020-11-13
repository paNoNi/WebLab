from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.get_usertask, name='tasks'),
    path('add', views.get_task_view)
]

