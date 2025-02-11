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

    favorites = models.ManyToManyField(
        'articles.Article',
        related_name='favorited_by'
    )

    def __str__(self):
        return self.user.username

    # Metodos para seguir

    def follow(self, profile):
        self.follows.add(profile)

    def unfollow(self, profile):
        self.follows.remove(profile)

    def is_following(self, profile):
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        return self.followed_by.filter(pk=profile.pk).exists()

    # Metodos favorito

    def favorite(self, article):
        self.favorites.add(article)

    def unfavorite(self, article):
        self.favorites.remove(article)

    def has_favorited(self, article):
        return self.favorites.filter(pk=article.pk).exists()
