from django.db import models

# Create your models here.


class Bookmark(models.Model):
    saved_url = models.URLField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    short_code = models.CharField(max_length=30)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']


class Click(models.Model):
    access_time = models.DateTimeField(auto_now_add=True)
    bookmarked_url = models.ForeignKey(Bookmark)

    class Meta:
        ordering = ['-access_time']

