from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from User.models import RedditUser
from Main.models import Subreddit

class RedditPost(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    user_posted = models.ForeignKey(
        RedditUser,
        on_delete=models.CASCADE,
        related_name='post_user'
        )
    subreddit_parent = models.ForeignKey(
        Subreddit,
        on_delete=models.CASCADE,
        related_name='subreddit_parent',
        null=True,
        blank=True
    )
    votes = models.IntegerField(default=0)
    users_voted = models.ManyToManyField(
        RedditUser,
        blank=True,
        related_name='user_voted'
    )

    dt_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(MPTTModel):
    content = models.TextField()
    user_commented = models.ForeignKey(
        RedditUser,
        on_delete=models.CASCADE,
        related_name='comment_user'
    )
    on_post = models.ForeignKey(
        RedditPost,
        on_delete=models.CASCADE,
        null=True
    )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    votes = models.IntegerField(default=0)
    users_voted = models.ManyToManyField(
        RedditUser,
        blank=True,
        related_name='users_voted'
    )

    dt_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
