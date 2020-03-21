from django.db import models
from authentication.models import User

from core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
