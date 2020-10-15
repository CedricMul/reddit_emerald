from django.shortcuts import render

from User.models import RedditUser
from Post.models import RedditPost, Comment

def user_view(request, username):
    user_id = RedditUser.objects.get(username=username).id
    user = RedditUser.objects.filter(id=user_id).first()
    posts = RedditPost.objects.filter(user_posted=user_id)
    comments = Comment.objects.filter(user_commented=user_id)
    return render(request, 'user.html', {
        'user': user,
        'posts': posts,
        'comments': comments
    })
