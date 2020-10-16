def is_mod(current_user, sub):
    if sub in current_user.subreddits_moderated:
        return True
    else:
        return False
