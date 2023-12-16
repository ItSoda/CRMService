from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Events
from users.models import Users

@receiver(post_save, sender=Events)
def update_user_field(sender, instance, created, **kwargs):
    if created:
        user = Users.objects.get(id=instance.creator.id)
        user.create_event = user.create_event + 1
        user.save()