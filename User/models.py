from django.db import models
from django.contrib.auth.models import AbstractUser

from Main.models import Subreddit

class RedditUser(AbstractUser):
    DisplayName = models.CharField(max_length=25, default='self')
    subscriptions = models.ManyToManyField(
        Subreddit,
        related_name='subscriptions',
        blank=True
        )
    subreddits_moderated = models.ManyToManyField(
        Subreddit,
        related_name='subreddits_moderated',
        blank=True
    )