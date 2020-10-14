from django.shortcuts import render
from django.shortcuts import render
from django.views import View

from Main.models import Subreddit

from Post.models import RedditPost

class indexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "all.html", {"subreddits": RedditPost.objects.all().order_by('votes')})
        user_subscriptions = request.user.subscriptions.all()
        user_subs = RedditPost.objects.filter(id__in=[sub.id for sub in user_subscriptions])
        return render(request, "all.html", {"subreddits": user_subs})