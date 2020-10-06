from django.db import models
#from User.models import RedditUser

class Subreddit(models.Model):
    name = models.CharField(max_length=80)
    # moderators = models.ManyToManyField(
    #     RedditUser,
    #     related_name='moderator',
    #     null=True
    # )
