from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View

from Post.models import RedditPost, Comment
from Post.forms import PostForm

from User.models import RedditUser

# Modified version of Ramon's views https://github.com/rhami223/reddit_emerald/blob/fd9ea13fc5f4775d5bfe6f52e72edd977d1ffc15/Post/views.py

def upvote_post_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    if not request.user in post.users_voted.all():
        post.votes += 1
        post.users_voted.add(request.user)
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def downvote_post_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    if not request.user in post.users_voted.all():
        post.votes -= 1
        post.users_voted.add(request.user)
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

##

def upvote_comment_view(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    if not request.user in c.users_voted.all():
        c.votes += 1
        c.users_voted.add(request.user)
        c.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def downvote_comment_view(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    if not request.user in c.users_voted.all():
        c.votes -= 1
        c.users_voted.add(request.user)
        c.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def post_detail_view(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    comments = Comment.objects.filter(on_post=post_id)
    return render(request, 'post_detail.html',{
        'post': post,
        'comments': comments
    })

def deletePost(request, post_id):
    post = RedditPost.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 

def post_form_view(request, sub_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = RedditPost.objects.create(
                title=data.get('title'),
                content=data.get('content'),
                url=data.get('url'),
                user_posted=request.user,
                subreddit_parent=Subreddit.objects.get(id=sub_id)
            )
            return HttpResponseRedirect("/post/{}/".format(new_post.id))
    form = PostForm()
    return render(request, 'generic_form.html', {'form': form})

def comment_form_view(request, post_id, comment_type, on_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if comment_type == 'reply':
                Comment.objects.create(
                    content=data.get('content'),
                    user_commented=request.user,
                    parent=Comment.objects.get(id=on_id),
                    on_post=RedditPost.objects.get(id=post_id)
                )
            elif comment_type == 'top_level':
                Comment.objects.create(
                    content=data.get('content'),
                    user_commented=request.user,
                    on_post=RedditPost.objects.get(id=on_id)
                )
            return HttpResponseRedirect("/post/{}/".format(post_id))
    form = CommentForm()
    return render(request, 'generic_form.html', {'form': form})

def delete_comment_view(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
