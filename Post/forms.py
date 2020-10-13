from django.forms import ModelForm
from Post.models import RedditPost, Comment

class PostForm(ModelForm):
    class Meta:
        model = RedditPost
        # fields = [
        #     'title',
        #     'content'
        # ]
        exclude = [
            'user_posted',
            'votes'
        ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = [
            'user_commented',
            'on_post',
            'replied_to',
            'votes'
        ]
