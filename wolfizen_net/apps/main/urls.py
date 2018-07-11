import os

from django.conf.urls import url
from django.http import FileResponse, Http404
from django.views.generic.base import View

from wolfizen_net.apps.main.views import *
from wolfizen_net.settings import TEMPLATE_DIR


class FileView(View):
    """
    This custom view will serve any specified file.

    as_view() accepts two arguments:
        file_path: The path to the file. Recommended to use `os.path.join(TEMPLATE_DIR, ...)`
        content_type: Passed into FileResponse().
    """

    file_path = None
    content_type = None

    def get(self, request, *args, **kwargs):
        try:
            return FileResponse(open(self.file_path, 'rb'), content_type=self.content_type)
        except FileNotFoundError:
            raise Http404()


app_name = "main"
urlpatterns = [
    url(r"^$", RootPageView.as_view(), name="root"),
    url(r"^infinite/(?P<depth>\d+)$", InfiniteRecursionView.as_view(), name="infinite-recursion"),
    url(r"^rainbow/$", RainbowTextView.as_view(), name="rainbow-text"),
    url(r"^keybase.txt$", FileView.as_view(file_path=os.path.join(TEMPLATE_DIR, "main/keybase.txt"), content_type="text/plain"), name="keybase"),
    url(r"^resume.pdf$", FileView.as_view(file_path=os.path.join(TEMPLATE_DIR, "main/resume.pdf"), content_type="application/pdf"), name="resume"),
]
