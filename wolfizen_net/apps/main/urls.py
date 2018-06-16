from django.conf.urls import include, url

from wolfizen_net.apps.main.views import *

app_name = "main"
urlpatterns = [
    url(r"^$", RootPageView.as_view(), name="root"),
    url(r"^infinite/(?P<depth>\d+)$", InfiniteRecursionView.as_view(), name="infinite-recursion"),
    url(r"^rainbow/$", RainbowTextView.as_view(), name="rainbow-text"),
    url(r"^keybase.txt$", TemplateView.as_view(template_name="main/keybase.txt", content_type="text/plain"), name="keybase"),
]
