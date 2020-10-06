from django.db import models
from django.contrib.auth.models import AbstractUser

from Main.models import Subreddit

class RedditUser(AbstractUser):
    subscriptions = models.ManyToManyField(
        Subreddit,
        related_name='subscriptions'
        )
    mod_permissions = models.ManyToManyField(
        Subreddit,
        related_name='mod_permissions'
    )


