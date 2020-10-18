from Main.models import Subreddit
from User.models import RedditUser

def is_mod(request, sub):
    if request.user.subreddits_moderated.filter(id=sub.id):
        return True
    else:
        return False
