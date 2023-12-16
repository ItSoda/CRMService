import uuid
from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from users.models import EmailPost, Users
from users.tasks import send_email_verify


# По любым вопросам к доке https://docs.djangoproject.com/en/4.2/ref/signals/
@receiver(post_save, sender=Users)
def user_post_save(created, **kwargs):
    instance = kwargs["instance"]
    if created:
        user = Users.objects.get(id=instance.id)
        send_email_verify.delay(user.id)