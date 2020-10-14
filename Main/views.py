from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from Main.models import Subreddit
from Post.models import RedditPost
from User.models import RedditUser
from Main.forms import SubredditForm

class indexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "all.html", {"subreddits": RedditPost.objects.all().order_by('votes')})
        user_subscriptions = request.user.subscriptions.all()
        user_subs = RedditPost.objects.filter(id__in=[sub.id for sub in user_subscriptions])
        return render(request, "all.html", {"subreddits": user_subs})

class SubredditView(DetailView):
    def get(self, request):
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
