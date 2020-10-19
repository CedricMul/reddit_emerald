from django.db import models

class Subreddit(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Subreddit, self).save(*args, **kwargs)

    def clean(self):
        if self.name:
            self.name = self.name.replace(' ', '')