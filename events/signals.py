import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import EmailPost, Users

from .models import Events
from .tasks import send_email_new


@receiver(post_save, sender=Events)
def update_user_field(sender, instance, created, **kwargs):
    if created:
        user = Users.objects.get(id=instance.creator.id)
        user.create_event = user.create_event + 1
        user.save()

        users = instance.participian.all()
        user_ids = [user.id for user in users]
        send_email_new.delay(user_ids=user_ids, instance_text=instance.text_for_email)
