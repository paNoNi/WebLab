from django.db import models
from Auth.models import Profile


class Task(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    date = models.DateField()
    object = models.CharField('Название предмета', max_length=50)
    image = models.ImageField("Изображение", upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.name


class UserTasks(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username
