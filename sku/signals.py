from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver

from sku.models import *


@receiver(post_save, sender=Location)
def is_signal_async(sender, instance, created, **kwargs):
    print("Signals are sync!")
