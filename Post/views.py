from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View

from Post.models import RedditPost, Comment
from Post.forms import PostForm

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

class PostFormView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "generic_form.html", {"form": form})
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = RedditPost.objects.create(
                title=data.get('title'),
                content=data.get('content'),
                url=data.get('url'),
                subreddit_parent=data.get('subreddit_parent'),
                user_posted=request.user
        )
        redirect_url = '/post/' + str(new_post.id) + '/'
        return HttpResponseRedirect(redirect_url)