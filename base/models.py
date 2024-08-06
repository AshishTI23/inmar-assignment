import uuid

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created_at = models.DateTimeField(("created_at"), auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(
        ("updated_at"), auto_now=True, auto_now_add=False
    )

    class Meta:
        abstract = True
