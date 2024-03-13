from celery import shared_task
from datetime import datetime,timedelta
from accounts.models import User
import uuid
from django.core.mail import EmailMessage
from django.conf import settings


@shared_task(name="AutomaticDeletion")
def delete_unverified_users():
    print(User.objects.filter(date_joined__lte = datetime.now() - timedelta(days=2)).delete(),"accounts are deleted today")

@shared_task
def send_mail(email,token=None):
    mail = EmailMessage(
        subject="Email Verification",
        body=f'Hi Click on this link to verify your mail http://127.0.0.1:8000/verify/{token}',
        from_email= settings.EMAIL_HOST_USER,
        to=[email],
    )
    mail.send()
