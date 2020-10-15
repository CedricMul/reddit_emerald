from django.db import models

from User.models import RedditUser
from Main.models import Subreddit

class RedditPost(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
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

    dt_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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

    dt_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content