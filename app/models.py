from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Bookmark(models.Model):
    saved_url = models.URLField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    short_code = models.CharField(max_length=30)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-time_created']

    @property
    def click_count(self):
        return self.click_set.all().count()


class Click(models.Model):
    clicked = models.BooleanField(default=True)
    bookmarked_url = models.ForeignKey(Bookmark)
