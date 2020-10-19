from django.forms import ModelForm
from Main.models import Subreddit

class SubredditForm(ModelForm):
    class Meta:
        model = Subreddit
        fields = ['name']