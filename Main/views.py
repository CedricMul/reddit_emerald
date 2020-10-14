from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from Main.models import Subreddit
from Post.models import RedditPost
from User.models import RedditUser
from Main.forms import SubredditForm

class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "all.html", {"posts": RedditPost.objects.all().order_by('votes')})
        user_subscriptions = request.user.subscriptions.all()
        user_subs = RedditPost.objects.filter(id__in=[sub.id for sub in user_subscriptions])
        return render(request, "all.html", {"posts": user_subs})

#r/all/
class AllView(View):
    def get(self, request):
        posts = RedditPost.objects.all().order_by('-votes')
        return render(request, 'all.html', {'posts': posts})

def filter_view(request, sub, sub_filter):
    filter_dict = {
        #'recent': RedditPost.objects.filter(subreddit_parent=sub).order_by('-date_and_time'),
        'popular': RedditPost.objects.filter(subreddit_parent=sub).order_by('-votes'),
        'least_popular': RedditPost.objects.filter(subreddit_parent=sub).order_by('votes'),
    }
    posts = filter_dict[sub_filter]
    return render(request, 'all.html', {'posts': posts})

def search_view(request, search):
    if Subreddit.objects.get(name=search):
        HttpResponseRedirect('/r/{}'.format(search))
    else:
        HttpResponseRedirect(reverse('homepage'))

def subreddit_view(request, sub):
    posts = RedditPost.objects.filter(subreddit_parent=sub).order_by('-votes')
    return(request, 'all.html', {'posts': posts})

class SubredditFormView(TemplateView):
    def get(self, request):
        form = SubredditForm()
        return render(request, 'form.html', {'form': form})
    
    def post(self, request):
        form = SubredditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_sub = Subreddit.objects.create(
                name=data.get('name')
            )
            request.user.subreddits_moderated.add(new_sub)
            return HttpResponseRedirect('/r/{}/'.format(new_sub))
