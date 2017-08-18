from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from wolfizen_net.views import *

urlpatterns = [
    url(r"^$", RootPageView.as_view(), name="root"),
    url(r"^infinite/(?P<depth>\d+)$", InfiniteRecursionView.as_view(), name="infinite-recursion"),
    url(r"^rainbow/$", RainbowTextView.as_view(), name="rainbow-text"),
    url(r"^rsfa-voting/$", ShowListView.as_view(), name="rsfa-voting"),
    url(r"^rsfa-voting/new/$", CreateShowView.as_view(), name="rsfa-voting-new-show"),
    url(r"^rsfa-voting/vote/$", csrf_exempt(VoteView.as_view()), name="rsfa-voting-vote"),
    url(r"^admin/", admin.site.urls),
]
