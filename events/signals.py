import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Events
from users.models import EmailPost, Users

@receiver(post_save, sender=Events)
def update_user_field(sender, instance, created, **kwargs):
    if created:
        user = Users.objects.get(id=instance.creator.id)
        user.create_event = user.create_event + 1
        user.save()

        users = Users.objects.all()
        for user in users:
            if instance.text_for_email is not None:
                record = EmailPost.objects.create(
                    code=uuid.uuid4(), user=user, text=instance.text_for_email
                )
                record.send_email_everyone()
            else:
                break

