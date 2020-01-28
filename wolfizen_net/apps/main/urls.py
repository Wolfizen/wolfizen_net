import os

from django.conf import settings
from django.conf.urls import url

from wolfizen_net.apps.main.views import *


app_name = "main"
urlpatterns = [
    url(r"^$", RootPageView.as_view(), name="root"),
    url(r"^infinite/(?P<depth>\d+)$", InfiniteLinksView.as_view(), name="infinite-links"),
    url(r"^rainbow/$", RainbowTextView.as_view(), name="rainbow-text"),
    url(r"^keybase.txt$", FileView.as_view(
        file_path=os.path.join(settings.TEMPLATE_DIR, "main/keybase.txt"), content_type="text/plain"), name="keybase"),
    url(r"^resume.pdf$", FileView.as_view(
        file_path=os.path.join(settings.TEMPLATE_DIR, "main/resume.pdf"), content_type="application/pdf"), name="resume"),
]
