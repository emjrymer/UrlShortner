from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from hashids import Hashids
from django.views.generic import View, ListView
from app.forms import BookmarkForm
from app.models import Click, Bookmark


class FirstView(View):

    def get(self, request):
        bookmark_form = BookmarkForm()
        all_bookmarks = Bookmark.objects.all()
        return render(request, 'index.html', {'form': bookmark_form, 'all_bookmarks': all_bookmarks})

    def post(self, request):
        form_instance = BookmarkForm(request.POST)
        hashids = Hashids()
        if form_instance.is_valid():
            new_form_instance = form_instance.save()
            new_form_instance.short_code = hashids.encode(new_form_instance.id)
            new_form_instance.save()
            Click.objects.create(bookmarked_url=Bookmark(new_form_instance.id), access_time=datetime.now())
            return render(request, 'index.html', {'url': new_form_instance, 'clicks': Click.objects.all()})


def new_link(request, short_code):
    bookmark = Bookmark.objects.get(short_code=short_code)
    new_click = Click.objects.create(bookmarked_url=bookmark.saved_url, access_time=datetime.now())
    new_click.save()
    return HttpResponseRedirect(reverse(bookmark.saved_url))


class BookmarkListView(ListView):
    model = Bookmark


class ClickListView(ListView):
    model = Click
