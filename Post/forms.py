from django.forms import ModelForm
from Post.models import RedditPost, Comment

class PostForm(ModelForm):
    class Meta:
        model = RedditPost
        exclude = [
            'user_posted',
            'users_voted',
            'sub',
            'votes',
            'subreddit_parent',
            'dt_time'
        ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = [
            'user_commented',
            'on_post',
            'replied_to',
            'votes',
            'parent',
            'users_voted',
            'dt_time'
        ]
