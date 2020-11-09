from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30)
    date_of_birth = models.DateField()
    photo = models.ImageField('Фото', upload_to='images/photos/', default='images/photos/empty_photo')

    def __str__(self):
        return self.name
