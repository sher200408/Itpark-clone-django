from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import Profil



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profil.objects.create(
            profil=user
        )


@receiver(post_save, sender=Profil)
def user_edit(sender, instance, created, **kwargs):
        user = instance.user
        if instance.name and len(instance.name.split(" ")) == 2:
            user.first_name, user.last_name = instance.name.split(" ")
        if instance.email:
            user.email = instance.email
        user.save()