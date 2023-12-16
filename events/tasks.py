import uuid

from celery import shared_task

from users.models import EmailPost, Users


@shared_task
def send_email_new(user_ids, instance_text):
    if instance_text is not None:
        for user_id in user_ids:
            user = Users.objects.get(id=user_id)
            record = EmailPost.objects.create(
                code=uuid.uuid4(), user=user, text=instance_text
            )
            record.send_email_everyone()
