from django.db import models
#from User.models import RedditUser
from Post.models import RedditPost

class Subreddit(models.Model):
    name = models.CharField(max_length=80)
    # moderators = models.ManyToManyField(
    #     RedditUser,
    #     related_name='moderator',
    #     null=True
    # )
    posts = models.ManyToManyField(
        RedditPost,
        related_name='sub_posts',
        #null=True,
        #blank=True
    )
