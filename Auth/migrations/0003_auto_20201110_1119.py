# Generated by Django 3.1.2 on 2020-11-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20201110_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='photos/empty_photo.jpg', upload_to='photos/', verbose_name='Аватар'),
        ),
    ]
