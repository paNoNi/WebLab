# Generated by Django 3.1.2 on 2020-11-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sod', '0002_auto_20201109_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='../static/src/default.jpg', upload_to='images/', verbose_name='Изображение'),
        ),
    ]
