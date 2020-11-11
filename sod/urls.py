from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.UserTasksView.as_view()),
    path('add', views.AddTask.as_view())
]
