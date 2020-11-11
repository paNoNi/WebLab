from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    photo = models.ImageField("Аватар", upload_to='photos/', default='photos/empty_photo.jpg')

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.user.id})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)#, id=instance.id)

@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()