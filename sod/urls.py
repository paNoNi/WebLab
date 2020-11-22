from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.get_usertask, name='tasks'),
    path('add', views.save_task, name='add'),
    path('description-<int:pk>', views.DescriptionDetail.as_view(), name='description'),
    path('updatetask-<int:pk>', views.TaskDetailView.as_view()),
    path('deletetask-<int:pk>', views.TaskDeleteView.as_view())
]

