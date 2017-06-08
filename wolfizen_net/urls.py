from django.conf.urls import url
from django.contrib import admin

from wolfizen_net.views import RootPageView

urlpatterns = [
    url(r"^", RootPageView.as_view(), name="root"),
    url(r"^admin/", admin.site.urls),
]
