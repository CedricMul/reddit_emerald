from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import RedditPost
# Create your views here.
def upvotes_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.upvotes = F('upvotes') + 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def downvote_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.downvotes = F('downvotes') + 1
    post.save()
    return HttpResponseRedirect(reverse('home'))