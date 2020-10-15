from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View

from Post.models import RedditPost

from User.models import RedditUser

# Modified version of Ramon's views https://github.com/rhami223/reddit_emerald/blob/fd9ea13fc5f4775d5bfe6f52e72edd977d1ffc15/Post/views.py

def upvote_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def downvote_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.votes -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

##

def user_view(request, username):
    user_id = RedditUser.objects.get(username=username).id
    user = RedditUser.objects.filter(id=user_id).first()
    return render(request, 'user.html', {'user': user})