from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    date = models.DateField()
    object = models.CharField('Название предмета', max_length=50)
    image = models.ImageField("Изображение", upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.name
