"""url_shortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views import new_link, BookmarkListView, BookmarkDetailView, BookmarkCreateView, BookmarkUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark_detail/(?P<pk>\d+)', BookmarkDetailView.as_view(), name="bookmark_detail_view"),
    url(r'^bookmark_create/$', BookmarkCreateView.as_view(), name="first_view"),
    url(r'^list/$', BookmarkListView.as_view(), name="bookmark_list_view"),
    url(r'^e/(?P<short_code>\w+)/$', new_link, name='new_link'),
    url(r'^accounts/login/$', auth_views.login, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, name="logout"),
    url(r'^update/(?P<pk>\d+)', BookmarkUpdateView.as_view(), name='bookmark_update_view')
]