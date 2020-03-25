from django.db import models
from profiles.models import Profile
from core.models import TimestampedModel


class Article(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='articles'
    )

    def __str__(self):
        return self.title
