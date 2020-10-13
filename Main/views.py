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
        if request.user.is_authenticated:
            subs = request.user.subscriptions
            posts = RedditPost.objects.filter(subreddit__in=subs).order_by('-votes')
            return render(request, 'all.html', {'posts': posts})
        else:
            return HttpResponseRedirect('/r/all/')

class SubredditView(DetailView):
    def get(self, request):
        posts = Subreddit.objects.filter(name=sub).posts.all().order_by('-votes')
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
            request.user.mod_permissions.add(new_sub)
            return HttpResponseRedirect('/r/{}/'.format(data.get('name')))
