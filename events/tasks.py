import uuid
from celery import shared_task

from users.models import EmailPost


@shared_task
def send_email_new(users, instance):
    if instance.text_for_email is not None:
        for user in users:
            record = EmailPost.objects.create(
                code=uuid.uuid4(), user=user, text=instance.text_for_email
            )
            record.send_email_everyone()