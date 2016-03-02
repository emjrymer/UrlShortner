from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from hashids import Hashids
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from app.forms import BookmarkForm
from app.models import Click, Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ('saved_url', 'title', 'description')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        hashids = Hashids(min_length=5)
        hashid = hashids.encode(object.id)
        object.short_code = hashid
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bookmark_list_view')


class BookmarkListView(ListView):
    model = Bookmark


def new_link(request, url):
    bookmark = Bookmark.objects.get(short_code=url)
    return HttpResponseRedirect(bookmark.saved_url)


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ('saved_url', 'title', 'description')

    def get_success_url(self):
        return reverse("first_view")


class BookmarkDetailView(DetailView):
    model = Bookmark

    def get_object(self):
        object = super().get_object()
        Click.objects.create(bookmarked_url=object)
        return object
