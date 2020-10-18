from Main.models import Subreddit

def is_mod(current_user, sub):
    if Subreddit.objects.filter(subreddits_moderated__id=current_user.id):
        return True
    else:
        return False
