from django.db import models

from Main.models import Subreddit
from User.models import RedditUser

class RedditPost(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    user_posted = models.ForeignKey(
        RedditUser,
        on_delete=models.CASCADE,
        related_name='post_user'
        )
    sub = models.ForeignKey(
        Subreddit,
        on_delete=models.CASCADE
    )
    votes = models.IntegerField(default=0)

class Comment(models.Model):
    content = models.TextField()
    user_commented = models.ForeignKey(
        RedditUser,
        on_delete=models.CASCADE,
        related_name='comment_user'
    )
    on_post = models.ForeignKey(
        RedditPost,
        on_delete=models.CASCADE
    )
    replied_to = models.ForeignKey(
        to='Comment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='op'
    )
    votes = models.IntegerField(default=0)
