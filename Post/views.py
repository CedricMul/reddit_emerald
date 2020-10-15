from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View

from Post.models import RedditPost, Comment

from User.models import RedditUser

# Modified version of Ramon's views https://github.com/rhami223/reddit_emerald/blob/fd9ea13fc5f4775d5bfe6f52e72edd977d1ffc15/Post/views.py

def upvote_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.votes += 1
    post.save()
    return HttpResponseRedirect(request.GET.next)

def downvote_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.votes -= 1
    post.save()
    return HttpResponseRedirect(request.GET.next)

def post_detail_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    comments = Comment.objects.filter(on_post=post_id).filter(replied_to__isnull=True)
    replies = Comment.objects.all()
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'replies': replies
    })
