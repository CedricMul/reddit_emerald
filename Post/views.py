from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View

from Post.models import RedditPost, Comment

from User.models import RedditUser

# Modified version of Ramon's views https://github.com/rhami223/reddit_emerald/blob/fd9ea13fc5f4775d5bfe6f52e72edd977d1ffc15/Post/views.py

def upvote_post_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.votes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def downvote_post_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.votes -= 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

##

def upvote_comment_view(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    c.votes += 1
    c.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def downvote_comment_view(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    c.votes -= 1
    c.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def post_detail_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    comments = Comment.objects.filter(on_post=post_id)
    return render(request, 'post_detail.html',{
        'post': post,
        'comments': comments
    })
