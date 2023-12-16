import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailPost, Users


@shared_task
def send_email_verify(user_id):
    user = Users.objects.get(id=user_id)
    expiration = now() + timedelta(hours=24)
    record = EmailPost.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()