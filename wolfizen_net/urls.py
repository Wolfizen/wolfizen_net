from django.conf.urls import url
from django.contrib import admin

from wolfizen_net.views import *

urlpatterns = [
    url(r"^$", RootPageView.as_view(), name="root"),
    url(r"^infinite/(?P<depth>\d+)$", InfiniteRecursionView.as_view(), name="infinite-recursion"),
    url(r"^admin/", admin.site.urls),
]
