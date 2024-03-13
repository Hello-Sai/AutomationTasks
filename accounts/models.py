from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=50)
        
@receiver(post_save,sender=User)
def account_verification(sender, instance=None, created=False, **kwargs):
    from accounts.tasks import send_mail

    if created:
        send_mail.delay(instance.email,instance.token)
@receiver(pre_save,sender=User)
def account_creation(sender,instance=None,*args,**kwargs):
    instance.username = instance.username