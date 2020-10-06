from django.contrib import admin
from Post.models import RedditPost, Comment

admin.site.register(RedditPost)
admin.site.register(Comment)
