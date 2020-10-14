from django.shortcuts import render
from django.views import View
from Main.models import Subreddit
from django.db.models import F
class indexView(View):
    def get(self, request):
        return render(request, "index.html", {"subreddits": Subreddit.all()})

def sort_view(request):
    post = BoastRoast.objects.order_by(
        -(F('upvotes') - F('downvotes'))
    )
    return render(request, 'sort.html', {'posts': post})