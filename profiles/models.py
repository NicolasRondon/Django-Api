from django.db import models
from authentication.models import User

from core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False)

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.follows.add(profile)

    def unfollow(self, profile):
        self.follows.remove(profile)

    def is_following(self, profile):
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        return self.followed_by.filter(pk=profile.pk).exists()